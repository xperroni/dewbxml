#! /usr/bin/env python
#coding=utf-8

r'''Converter of Wireless Binary XML (WBXML) documents to plain-text XML.

    When invoked without arguments, DeWBXML opens one file dialog asking for an
    input WBXML file, and another for defining the path to the output plain-text
    XML file. Execution is terminated if any of those dialogs is canceled.

    Alternatively, the program can be invoked from command line with either two
    arguments (the input and output paths) or just one (in which case the output
    is written to standard output).
'''

__license__ = r'''
Copyright (c) 2025 Helio Perroni Filho

This file is part of DeWBXML.

DeWBXML is distributed under the terms of the MIT License.

You should have received a copy of the MIT License along with
DeWBXML. If not, see <https://choosealicense.com/licenses/mit/>.
'''

__version__ = '1.0.0'

import provisioning
import rightsobjects
import wml13

from base64    import b64encode
from sys       import stdout
from traceback import print_exc

# List of known charsets, indexed by their IANA numbers.
_charsets = {
      3: 'iso-ir-6',
      4: 'iso-ir-100',
      5: 'iso-ir-101',
      6: 'iso-ir-109',
      7: 'iso-ir-110',
      8: 'iso-ir-144',
      9: 'iso-ir-127',
     10: 'iso-ir-126',
    106: 'utf-8'
}

# List of known WBXML encondings for plain-text XML applications.
_applications = {
    0x0B: provisioning.encoding,
    0x0E: rightsobjects.encoding,
    0x04: wml13.encoding
}

# Special WBXML tokens.
SWITCH_PAGE = 0x00
END         = 0x01
STR_I       = 0x03
STR_T       = 0x83
OPAQUE      = 0xC3


class wbxmldocument(object):
    r'''Class for WBXML DOM document objects.
    '''
    def __init__(self):
        r'''Creates a new WBXML DOM document object.
        '''
        self.encoding = ''
        self.schema = ''
        self.version = ''
        self.__stringtable = []
        self.root = None

    def __str__(self):
        r'''Converts this document object (and contained element objects,
            recursively) to string.
        '''
        return \
            r'<?xml version="1.0" encoding="' + self.encoding + r'"?>' + \
            '\n\n' + \
            r'<!DOCTYPE ' + self.schema + r'>' + \
            '\n\n' + \
            r'<!-- WBXML version: ' + self.version + r' -->' + \
            '\n\n' + \
            r'<!-- Contents of string table: "' + str(self.stringtable) + r'" -->' + \
            '\n\n' + \
            str(self.root)

    def addchild(self, root):
        r'''Sets this document's root object. It's a convenience method meant
            for easing the implementation of the DOM parser.
        '''
        self.root = root
        root.parent = self

    @property
    def stringtable(self):
        string = ''
        table = []
        for code in self.__stringtable:
            if code != 0x00:
                string += chr(code)
            else:
                table.append(string)
                string = ''

        return table

    @stringtable.setter
    def stringtable(self, table):
        self.__stringtable = table


class wbxmlelement(object):
    r'''Class for WBXML DOM elements.
    '''
    def __init__(self, name = None, attributes = {}):
        r'''Creates a new WBXML DOM element object.
        '''
        self.parent = None
        self.name = name
        self.attributes = dict(attributes)
        self.children = []

    def __str__(self):
        r'''Converts this element object (and contained element objects,
            recursively) to string.
        '''
        return self.tostring(0)

    def tostring(self, level):
        r'''Converts this element object (and contained element objects,
            recursively) to string, idented to the given ident level.
        '''
        ident = level * '  '
        attributes = ''
        for (name, value) in self.attributes.items():
            attributes += ' ' + name + '="' + value + '"'

        closebracket = ''
        children = ''
        closetag = ''

        if len(self.children) > 0:
            closebracket = '>\n'
            closetag = ident + '</' + self.name + '>'
            for child in self.children:
                children += child.tostring(level + 1)
        else:
            closebracket = ' />'

        return ident + '<' + self.name + attributes + closebracket + children + closetag + '\n'

    def addchild(self, child):
        r'''Adds a child element to this element object.
        '''
        self.children.append(child)
        child.parent = self


class wbxmlstring(object):
    r'''Class for text elements.
    '''
    def __init__(self, value):
        r'''Creates a new text element object from a string.
        '''
        self.__value = value

    def __str__(self):
        r'''Converts this text element to string.
        '''
        return self.tostring(0)

    def tostring(self, level):
        r'''Converts this text element to string, idented to the given ident
            level.
        '''
        return level * '  ' + self.__value + '\n'


class wbxmlreader(object):
    r'''File reader for WBXML documents. Implements several conveniences for
        parsing WBXML files.
    '''
    def __init__(self, path):
        r'''Creates a new WBXML reader for the file at the given path.
        '''
        self.__bytes = open(path, 'rb')

    def __iter__(self):
        r'''Returns an iterator over this reader (actually, the object itself).
        '''
        return self

    def next(self):
        r'''Reads one binary token from the WBXML file and advances the file
            pointer one position. If the end-of-file has already been reached,
            raises the StopIteration exception.
        '''
        return self.read()

    def read(self, length = None):
        r'''Reads a sequence of one or more tokens from the underlying WBXML
            file, incrementing the file pointer accordingly.

            If the length is ommited, one token is read and returned as an
            integer; otherwise, at most (length) tokens are read and returned as
            a character string. This holds true even for length = 1, so
            reader.read(1) returns a single-character string.

            If a previous operation reached the end-of-file, this method raises
            the StopIteration exception.
        '''
        data = self.__bytes.read(1 if length == None else length)

        if len(data) == 0:
            raise StopIteration()

        return ord(data) if length == None else data

    def readopaque(self):
        r'''Reads an opaque data buffer from the WBXML file, and returns it
            as a base64 string. The file pointer is incremented until past the
            end of the buffer.
        '''
        length = self.read()
        data = self.read(length)
        return b64encode(data)

    def readstring(self):
        r'''Reads tokens from the WBXML file until the end-of-string character
            (0x00) is reached, returning the result as a string. The file
            pointer is incremented until past the end-of-string character.
        '''
        data = ''
        while True:
            char = self.read(1)
            if char == '\0':
                return data
            data += char


class wbxmlparser(object):
    r'''A DOM parser for Wireless Binary XML documents.
    '''
    def __init__(self, applications={}, charsets={}):
        r'''Creates a new parser object.
        '''
        self.__applications = dict(_applications)
        self.__applications.update(applications)

        self.__charsets = dict(_charsets)
        self.__charsets.update(charsets)

        self.__encoding = None
        self.__page = 0
        self.__strings = []

    def parse(self, data):
        r'''Parses a WBXML file and returns a WBXML DOM document object.

            If data is a string, it is interpreted as a path to a WBXML file;
            otherwise, it's expected to be a wbxmlreader object.
        '''
        if isinstance(data, basestring):
            data = wbxmlreader(data)

        doc = wbxmldocument()
        try:
            self.__version(data, doc)
            self.__publicid(data, doc)
            self.__charset(data, doc)
            self.__stringtable(data, doc)
            self.__body(data, doc)
        except Exception as e:
            print_exc(file=stdout)

        return doc

    def __get(self, *keys):
        r'''Walks the current WBXML token specification, returning the object
            (either leaf or subtree) at the end of the path.

            If the path is not found, raises a KeyError exception.
        '''
        data = self.__encoding['elements']
        try:
            for key in keys:
                data = data[key]
            return data
        except:
            raise KeyError('(' + ', '.join([hex(k) for k in keys]) + ')')

    def __version(self, data, doc):
        r'''Sets the version attribute of a WBXML DOM document object.
        '''
        token = data.read()
        minor = 0b1111 & token
        major = (token >> 4) + 1
        doc.version = `major` + '.' + `minor`

    def __publicid(self, data, doc):
        r'''Sets the schema attribute of a WBXML DOM document object. Also sets
            the active WBXML token specification.
        '''
        token = data.read()
        self.__encoding = self.__applications[token]
        doc.schema = self.__encoding['dtd']

    def __charset(self, data, doc):
        r'''Sets the encoding attribute of a WBXML DOM document object.
        '''
        token = data.read()
        doc.encoding = self.__charsets[token]

    def __stringtable(self, data, doc):
        r'''Sets the string table of a WBXML DOM document object.
        '''
        length = data.read()
        self.__strings = [data.read() for i in range(0, length)]
        doc.stringtable = self.__strings

    def __readstringtable(self, offset):
        table = self.__strings
        string = ''
        for i in range(offset, len(table)):
            code = table[i]
            if code != 0x00:
                string += chr(code)
            else:
                break

        return string

    def __body(self, data, doc):
        r'''Parses the body of a WBXML document, constructing the element DOM
            tree.
        '''
        self.__elements(data, doc)

    def __elements(self, data, parent):
        r'''Parses the children of a parent WBXML element, as well as their
            children recursively.
        '''
        for token in data:
            node = None
            if token == END:
                return
            elif token == STR_I:
                node = wbxmlstring(data.readstring())
            elif token == OPAQUE:
                node = wbxmlstring(data.readopaque())
            else:
                (tag, hasattributes, hascontents) = (
                    (0b00111111 & token),               # Base tag code
                    ((0b10000000 & token) >> 7) == 1,   # "Has attributes" bit
                    ((0b01000000 & token) >> 6) == 1    # "Has contents" bit
                )

                name = self.__get(self.__page, tag, 0)
                node = wbxmlelement(name)
                if hasattributes:
                    self.__attributes(data, tag, node)
                if hascontents:
                    self.__elements(data, node)
            parent.addchild(node)

    def __attributes(self, data, element, node):
        r'''Parses the attributes of a WBXML element.
        '''
        for token in data:
            if token == END:
                return
            elif token == SWITCH_PAGE:
                self.__page = data.read()
            else:
                self.__value(data, element, token, node)

    def __value(self, data, element, attribute, node):
        (name, value) = self.__get(self.__page, element, 1, attribute)
        if value != None and not (isinstance(value, dict) or callable(value)):
            node.attributes[name] = value
            return

        token = data.read()
        if token == STR_I:
            node.attributes[name] = data.readstring()
        elif token == STR_T:
            offset = data.read()
            node.attributes[name] = self.__readstringtable(offset)
        elif value == None:
            node.attributes[name] = str(token)
        elif isinstance(value, dict):
            node.attributes[name] = value[token]
        else:
            node.attributes[name] = value(node, token)


def dialog():
    r'''Opens the input and output file dialogs, then calls the parse() function.
    '''
    from Tkinter import Tk
    import tkFileDialog
    root = Tk()
    root.withdraw()

    from sys import stdin, stdout

    stdout.write('Path to the input WBXML file: ')

    binary = tkFileDialog.askopenfilename(
        master = root,
        title = 'Open WBXML File',
        filetypes = [('Wireless Binary XML', '.wbxml'), ('All Files', '*')]
    )

    if binary == '':
        root.quit()
        return

    stdout.write(binary + '\n\n')

    stdout.write('Path to the output plain-text XML file: ')

    plain = tkFileDialog.asksaveasfilename(
        master = root,
        title = "Save Plain-Text XML File",
        defaultextension = ".xml",
        filetypes = [('Plain-Text XML', '.xml'), ('All Files', '*')]
    )

    if plain == '':
        root.quit()
        return

    stdout.write(plain + '\n\n')

    root.quit()

    stdout.write('Decoding WBXML file... ')

    parse(binary, plain)

    stdout.write('Done.')
    stdin.read()


def parse(binary, plain = None):
    r'''Parses an input WBXML file. Results are written to a plain-text output
        file if it is given; otherwise, the standard output is used.
    '''
    wbxml = wbxmlparser().parse(binary)
    out = open(plain, 'w') if plain != None else stdout
    out.write(str(wbxml))
    if hasattr(out, 'close'):
        out.close()


def main():
    r'''Function invoked when this module is ran as a script.
    '''
    import sys
    if len(sys.argv) > 1:
        parse(*sys.argv[1:])
    else:
        dialog()


# Command-line entry point
if __name__ == '__main__':
    main()

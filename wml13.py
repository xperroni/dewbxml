#coding=utf-8

r'''WBXML specification for the rights object format.
'''

__license__ = r'''
Copyright (c) 2025 Helio Perroni Filho

This file is part of DeWBXML.

DeWBXML is distributed under the terms of the MIT License.

You should have received a copy of the MIT License along with
DeWBXML. If not, see <https://choosealicense.com/licenses/mit/>.
'''

__version__ = '1.0.0'

#TODO: Figure out what to do with the extension tokens:
#EXT_I_0 = 0x40 # Variable substitution - escaped. Name of the variable is inline and follows the token as a termstr.
#EXT_I_1 = 0x41 # Variable substitution - unescaped. Name of the variable is inline and follows the token as a termstr.
#EXT_I_2 = 0x42 # Variable substitution - no transformation. Name of the variable is inline and follows the token as a termstr.
#EXT_T_0 = 0x80 # Variable substitution - escaped. Variable name encoded as a reference into the string table.
#EXT_T_1 = 0x81 # Variable substitution - unescaped. Variable name encoded as a reference into the string table.
#EXT_T_2 = 0x82 # Variable substitution - no transformation. Variable name encoded as a reference into the string table.
#EXT_0   = 0xC0 # Reserved for future use.
#EXT_1   = 0xC1 # Reserved for future use.
#EXT_2   = 0xC2 # Reserved for future use.


#TODO: Figure out what to do with the attribute value tokens:
#0x85: '.com/',
#0x86: '.edu/',
#0x87: '.net/',
#0x88: '.org/',
#0x89: 'accept',
#0x8A: 'bottom',
#0x8B: 'clear',
#0x8C: 'delete',
#0x8D: 'help',
#0x8E: 'http://',
#0x8F: 'http://www.',
#0x90: 'https://',
#0x91: 'https://www.',
#0x93: 'middle',
#0x94: 'nowrap',
#0x96: 'onenterbackward',
#0x97: 'onenterforward',
#0x95: 'onpick',
#0x98: 'ontimer',
#0x99: 'options',
#0x9A: 'password',
#0x9B: 'reset',
#0x9D: 'text',
#0x9E: 'top',
#0x9F: 'unknown',
#0xA0: 'wrap',
#0xA1: 'Www.',


encoding = {
    # The XML application's DTD string.
    'dtd': r'wml PUBLIC "-//WAPFORUM//DTD WML 1.3//EN" "http://www.wapforum.org/DTD/wml13.dtd"',

    # Token codes for the XML application's elements.
    'elements': [
        { # Page 0
            0x1C: ('a', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x4A: ('href', None),
                    0x5E: ('accesskey', None)
                }
            ),
            0x22: ('anchor', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x36: ('title', None),
                    0x5E: ('accesskey', None)
                }
            ),
            0x23: ('access', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x0F: ('domain', None),
                    0x2A: ('path', None)
                }
            ),
            0x24: ('b', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None)
                }
            ),
            0x25: ('big', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None)
                }
            ),
            0x26: ('br', {
                    0x55: ('id', None),
                    0x54: ('class', None)
                }
            ),
            0x27: ('card', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x36: ('title', None),
                    0x22: ('newcontext', 'false'),
                    0x23: ('newcontext', 'true'),
                    0x33: ('ordered', 'true'),
                    0x34: ('ordered', 'false'),
                    0x27: ('ontimer', None),
                    0x25: ('onenterbackward', None),
                    0x26: ('onenterforward', None)
                }
            ),
            0x28: ('do', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x37: ('type', None),
                    0x38: ('type', 'accept'),
                    0x39: ('type', 'delete'),
                    0x3A: ('type', 'help'),
                    0x3B: ('type', 'password'),
                    0x3C: ('type', 'onpick'),
                    0x3D: ('type', 'onenterbackward'),
                    0x3E: ('type', 'onenterforward'),
                    0x3F: ('type', 'ontimer'),
                    0x45: ('type', 'options'),
                    0x46: ('type', 'prev'),
                    0x47: ('type', 'reset'),
                    0x48: ('type', 'text'),
                    0x49: ('type', 'vnd.'),
                    0x18: ('label', None),
                    0x21: ('name', None),
                    0x28: ('optional', 'false'),
                    0x29: ('optional', 'true')
                }
            ),
            0x29: ('em', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None)
                }
            ),
            0x2A: ('fieldset', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x36: ('title', None)
                }
            ),
            0x2B: ('go', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x4A: ('href', None),
                    0x2F: ('sendreferer', 'false'),
                    0x30: ('sendreferer', 'true'),
                    0x1B: ('method', 'get'),
                    0x1C: ('method', 'post'),
                    0x64: ('cache-control', 'no-cache'),
                    0x5F: ('enctype', None),
                    0x60: ('enctype', 'application/x-www-form-urlencoded'),
                    0x61: ('enctype', 'multipart/for'),
                    0x05: ('accept-charset', None)
                }
            ),
            0x2C: ('head', {
                    0x55: ('id', None),
                    0x54: ('class', None)
                }
            ),
            0x2D: ('i', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None)
                }
            ),
            0x2E: ('img', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x0C: ('alt', None),
                    0x32: ('src', None),
                    0x58: ('src', 'http://'),
                    0x59: ('src', 'https://'),
                    0x19: ('localsrc', None),
                    0x4E: ('vspace', None),
                    0x14: ('hspace', None),
                    0x52: ('align', None),
                    0x06: ('align', 'bottom'),
                    0x07: ('align', 'center'),
                    0x08: ('align', 'left'),
                    0x09: ('align', 'middle'),
                    0x0A: ('align', 'right'),
                    0x0B: ('align', 'top'),
                    0x13: ('height', None),
                    0x4F: ('width', None),
                }
            ),
            0x2F: ('input', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x36: ('title', None),
                    0x35: ('tabindex', None),
                    0x5E: ('accesskey', None),
                    0x21: ('name', None),
                    0x4D: ('value', None),
                    0x48: ('type', 'text'),
                    0x3B: ('type', 'password'),
                    0x12: ('format', None),
                    0x10: ('emptyok', 'false'),
                    0x11: ('emptyok', 'true'),
                    0x31: ('size', None),
                    0x1A: ('maxlength', None)
                }
            ),
            0x30: ('meta', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x21: ('name', None),
                    0x5A: ('http-equiv', None),
                    0x5B: ('http-equiv', 'Content-Type'),
                    0x5D: ('http-equiv', 'Expires'),
                    0x56: ('forua', 'false'),
                    0x57: ('forua', 'true'),
                    0x0D: ('content', None),
                    0x5C: ('content', 'application/vnd.wap.wmlc;charset='),
                    0x2E: ('scheme', None)
                }
            ),
            0x31: ('noop', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                }
            ),
            0x20: ('p', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x52: ('align', None),
                    0x08: ('align', 'left'),
                    0x0A: ('align', 'right'),
                    0x07: ('align', 'center'),
                    0x1D: ('mode', 'nowrap'),
                    0x1E: ('mode', 'wrap')
                }
            ),
            0x21: ('postfield', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x21: ('name', None),
                    0x4D: ('value', None)
                }
            ),
            0x1B: ('pre', None),
            0x32: ('prev', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                }
            ),
            0x33: ('onevent', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x37: ('type', None),
                    0x38: ('type', 'accept'),
                    0x39: ('type', 'delete'),
                    0x3A: ('type', 'help'),
                    0x3B: ('type', 'password'),
                    0x3C: ('type', 'onpick'),
                    0x3D: ('type', 'onenterbackward'),
                    0x3E: ('type', 'onenterforward'),
                    0x3F: ('type', 'ontimer'),
                    0x45: ('type', 'options'),
                    0x46: ('type', 'prev'),
                    0x47: ('type', 'reset'),
                    0x48: ('type', 'text'),
                    0x49: ('type', 'vnd.'),
                }
            ),
            0x34: ('optgroup', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x36: ('title', None)
                }
            ),
            0x35: ('option', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x24: ('onpick', None),
                    0x4D: ('value', None),
                    0x36: ('title', None)
                }
            ),
            0x36: ('refresh', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                }
            ),
            0x37: ('select', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x35: ('tabindex', None),
                    0x20: ('multiple', 'true'),
                    0x21: ('name', None),
                    0x4D: ('value', None),
                    0x16: ('iname', None),
                    0x15: ('ivalue', None),
                    0x36: ('title', None)
                }
            ),
            0x38: ('small', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None)
                }
            ),
            0x3E: ('setvar', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x21: ('name', None),
                    0x4D: ('value', None)
                }
            ),
            0x39: ('strong', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None)
                }
            ),
            0x1F: ('table', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None),
                    0x36: ('title', None),
                    0x52: ('align', None),
                    0x06: ('align', 'bottom'),
                    0x07: ('align', 'center'),
                    0x08: ('align', 'left'),
                    0x09: ('align', 'middle'),
                    0x0A: ('align', 'right'),
                    0x0B: ('align', 'top'),
                    0x53: ('columns', None)
                }
            ),
            0x1D: ('td', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None)
                }
            ),
            0x3B: ('template',{
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x27: ('ontimer', None),
                    0x25: ('onenterbackward', None),
                    0x26: ('onenterforward', None)
                }
            ),
            0x3C: ('timer', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x21: ('name', None),
                    0x4D: ('value', None)
                }
            ),
            0x1E: ('tr', {
                    0x55: ('id', None),
                    0x54: ('class', None)
                }
            ),
            0x3D: ('u', {
                    0x55: ('id', None),
                    0x54: ('class', None),
                    0x50: ('xml:lang', None)
                }
            ),
            0x3F: ('wml', {
                    0x50: ('xml:lang', None)
                }
            )
		}
	]
}

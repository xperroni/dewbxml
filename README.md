# DeWBXML

**DeWBXML** is a Python application for decoding [WAP Binary XML (WBXML)](http://www.w3.org/TR/wbxml/) files. It was written with extensibility in mind: applications (e.g. WAP provisioning, WML, Push) are specified in Python using a style reminiscent of JSON, and plugged into a generic WBXML parser.

DeWBXML was created out of personal need for a simple, convenient WBXML decoder. As such, development follows a rather inconstant pace; new features are added only as their necessity arises. Contributions and bug reports are welcome, but no guarantees are made on responses, timely or otherwise.

## Installation and Usage

DeWBXML was written on Python 2.6.5; it may or may not work on other versions, though it can be reasonably expected to work on newer Python 2 interpreters. It is distributed as a bare collection of Python scripts; to install it, clone the repository to a directory of your liking, and setup your shell environment (`PYTHONPATH`, `PATH`, etc.) according to your preferences.

To run DeWBXML in command-line mode, open a command shell and type:

    python dewbxml.py <input WBXML file> <output plain-text XML file>

If the output path is not entered, DeWBXML writes the decoded XML to the standard output. If no arguments are provided, DeWBXML uses GUI file dialogs to ask for the input WBXML and output XML paths.

## Specifying Applications

WBXML applications are specified in Python according to the format below:

    encoding = {
        # The XML application's DTD string.
        'dtd': <DTD header>,

        # Token codes for the XML application's elements.
        'elements': [
            { # Page 0
                <element token>: (<element name>, {
                        <attribute token>: (<attribute name>, <attribute value>),
                        ...
                    }
                ),
                ...
            },

            { # Page 1
                <element token>: (<element name>, {
                        <attribute token>: (<attribute name>, <attribute value>),
                        ...
                    }
                ),
                ...
            }
        ]
    }

Where "tokens" are binary code values defined by the application's spec document, "names" are the corresponding XML tag names, and an attribute's value can be one of:

* A hard-coded value string;
* A dictionary mapping value tokens to value strings;
* A function which receives as arguments the element node object currently being parsed and a value token, and returns the decoded value string.

In some application spec documents, certain attributes are bound to multiple WBXML tokens, each representing a different pre-defined value. Accordingly, a single attribute may be specified multiple times, once for each token.

For examples on how to specify WBXML applications, look into files `provisioning.py`, `rightsobjects.py` and `wml13.py`. It's important to notice that, since applications are specified as Python code, they can be constructed and/or manipulated just as any ordinary Python object hierarchy; everything is fair game as long as the end result follows the above described form.

After an application is specified, it must be plugged into the parser. It can be hard-coded into the main `dewbxml.py` file (look for the module-level `_application` variable) or programmaticaly as in the example below:

    from dewbxml import wbxmlparser
    from example import encoding
    parser = wbxmlparser({<application token>: encoding})

Where `<application token>` is a binary code identifying the application (also found in the corresponding spec document).

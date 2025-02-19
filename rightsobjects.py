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

encoding = {
    # The XML application's DTD string.
    'dtd': r'o-ex:rights PUBLIC "-//OMA//DTD DRMREL 1.0//EN" "http://www.openmobilealliance.org/DTD/drmrel10.dtd"',

    # Token codes for the XML application's elements.
    'elements': [
        { # Page 0
            0x05: ('o-ex:rights', {
                    0x05: ('xmlns:o-ex', {
                            0x85: 'http://odrl.net/1.0/ODRL-EX'
                        }
                    ),
                    0x06: ('xmlns:o-dd', {
                            0x86: 'http://odrl.net/1.0/ODRL-DD'
                        }
                    ),
                    0x07: ('xmlns:ds', {
                            0x87: 'http://www.w3.org/2000/09/xmldsig#/'
                        }
                    )
                }
            ),
            0x06: ('o-ex:context', None),
            0x07: ('o-dd:version', None),
            0x08: ('o-dd:uid', None),
            0x09: ('o-ex:agreement', None),
            0x0A: ('o-ex:asset', None),
            0x0B: ('o-ex:cek', None),
            0x0C: ('o-ex:plainTextKey', None),
            0x0D: ('o-ex:permission', None),
            0x0E: ('o-dd:play', None),
            0x0F: ('o-dd:display', None),
            0x10: ('o-dd:execute', None),
            0x11: ('o-dd:print', None),
            0x12: ('o-ex:constraint', None),
            0x13: ('o-dd:count', None),
            0x14: ('o-dd:fixed', None),
            0x15: ('o-dd:datetime', None),
            0x16: ('o-dd:start', None),
            0x17: ('o-dd:end', None),
            0x18: ('o-dd:interval', None)
		}
	]
}

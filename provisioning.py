#coding=utf-8

r'''WBXML specification for the services provisioning format.
'''

__license__ = r'''
Copyright (c) 2025 Helio Perroni Filho

This file is part of DeWBXML.

DeWBXML is distributed under the terms of the MIT License.

You should have received a copy of the MIT License along with
DeWBXML. If not, see <https://choosealicense.com/licenses/mit/>.
'''

__version__ = '1.0.0'

_addrtype = [
    { # Page 0
        0x85: 'IPV4',
        0x86: 'IPV6',
        0x87: 'E164',
        0x88: 'ALPHA',
        0x89: 'APN',
        0x8A: 'SCODE',
        0x8B: 'TETRA-ITSI',
        0x8C: 'MAN'
    },

    { # Page 1
        0x86: 'IPV6',
        0x87: 'E164',
        0x88: 'ALPHA',
        0x8D: 'APPSRV',
        0x8E: 'OBEX'
    }
]

_authtype = [
    { # Page 0
        0x9A: 'PAP',
        0x9B: 'CHAP',
        0x9C: 'HTTP-BASIC',
        0x9D: 'HTTP-DIGEST',
        0x9E: 'WTLS-SS',
        0x9F: 'MD5'
    }
]


_values = {
    'ADRTYPE': _addrtype,
    'NAP-ADDRTYPE': _addrtype,
    'PXADDRTYPE': _addrtype,
    'LOCAL-ADDRTYPE': _addrtype,

    'CALLTYPE': [
        { # Page 0
            0x90: 'ANALOG-MODEM',
            0x91: 'V.120',
            0x92: 'V.110',
            0x93: 'X.31',
            0x94: 'BIT-TRANSPARENT',
            0x95: 'DIRECT-ASYNCHRONOUS-DATA-SERVICE'
        }
    ],

    'AUTHTYPE': _authtype,
    'PXAUTH-TYPE': _authtype,

    'BEARER': [
        { # Page 0
            0xA2: 'GSM-USSD',
            0xA3: 'GSM-SMS',
            0xA4: 'ANSI-136-GUTS',
            0xA5: 'IS-95-CDMA-SMS',
            0xA6: 'IS-95-CDMA-CSD',
            0xA7: 'IS-95-CDMA-PACKET',
            0xA8: 'ANSI-136-CSD',
            0xA9: 'ANSI-136-GPRS',
            0xAA: 'GSM-CSD',
            0xAB: 'GSM-GPRS',
            0xAC: 'AMPS-CDPD',
            0xAD: 'PDC-CSD',
            0xAE: 'PDC-PACKET',
            0xAF: 'IDEN-SMS',
            0xB0: 'IDEN-CSD',
            0xB1: 'IDEN-PACKET',
            0xB2: 'FLEX/REFLEX',
            0xB3: 'PHS-SMS',
            0xB4: 'PHS-CSD',
            0xB5: 'TETRA-SDS',
            0xB6: 'TETRA-PACKET',
            0xB7: 'ANSI-136-GHOST',
            0xB8: 'MOBITEX-MPAK',
            0xB9: 'CDMA2000-1X-SIMPLE-IP',
            0xBA: 'CDMA2000-1X-MOBILE-IP'
        }
    ],

    'LINKSPEED': [
        { # Page 0
            0xC5: 'AUTOBAUDING'
        }
    ],

    'SERVICE': [
        { # Page 0
            0xCA: 'CL-WSP',
            0xCB: 'CO-WSP',
            0xCC: 'CL-SEC-WSP',
            0xCD: 'CO-SEC-WSP',
            0xCE: 'CL-SEC-WTA',
            0xCF: 'CO-SEC-WTA',
            0xD0: 'OTA-HTTP-TO',
            0xD1: 'OTA-HTTP-TLS-TO',
            0xD2: 'OTA-HTTP-PO',
            0xD3: 'OTA-HTTP-TLS-PO'
        }
    ],

    'AAUTHTYPE': [
        { # Page 0
        },

        { # Page 1
            0x80: ',',
            0x81: 'HTTP-',
            0x82: 'BASIC',
            0x83: 'DIGEST'
        }
    ],

    'AUTH-ENTITY': [
        { # Page 0
            0xE0: 'AAA',
            0xE1: 'HA'
        }
    ]
}

encoding = {
    # The XML application's DTD string.
    'dtd': r'wap-provisioningdoc PUBLIC "-//WAPFORUM//DTD PROV 1.0//EN" "http://www.wapforum.org/DTD/prov.dtd"',

    # Token codes for the XML application's elements.
    'elements': [
        { # Page 0
            0x05: ('wap-provisioningdoc', {
                    0x45: ('version', None),
                    0x46: ('version', '1.0')
                }
            ),

            0x06: ('characteristic', {
                    0x50: ('type', None),
                    0x51: ('type', 'PXLOGICAL'),
                    0x52: ('type', 'PXPHYSICAL'),
                    0x53: ('type', 'PORT'),
                    0x54: ('type', 'VALIDITY'),
                    0x55: ('type', 'NAPDEF'),
                    0x56: ('type', 'BOOTSTRAP'),
                    0x57: ('type', 'VENDORCONFIG'),
                    0x58: ('type', 'CLIENTIDENTITY'),
                    0x59: ('type', 'PXAUTHINFO'),
                    0x5A: ('type', 'NAPAUTHINFO'),
                    0x5B: ('type', 'ACCESS')
                }
            ),

            0x07: ('parm', {
                    0x05: ('name', None),
                    0x06: ('value', lambda node, token: _values[node.attributes['name']][0][token]),
                    0x07: ('name', 'NAME'),
                    0x08: ('name', 'NAP-ADDRESS'),
                    0x09: ('name', 'NAP-ADDRTYPE'),
                    0x0A: ('name', 'CALLTYPE'),
                    0x0B: ('name', 'VALIDUNTIL'),
                    0x0C: ('name', 'AUTHTYPE'),
                    0x0D: ('name', 'AUTHNAME'),
                    0x0E: ('name', 'AUTHSECRET'),
                    0x0F: ('name', 'LINGER'),
                    0x10: ('name', 'BEARER'),
                    0x11: ('name', 'NAPID'),
                    0x12: ('name', 'COUNTRY'),
                    0x13: ('name', 'NETWORK'),
                    0x14: ('name', 'INTERNET'),
                    0x15: ('name', 'PROXY-ID'),
                    0x16: ('name', 'PROXY-PROVIDER-ID'),
                    0x17: ('name', 'DOMAIN'),
                    0x18: ('name', 'PROVURL'),
                    0x19: ('name', 'PXAUTH-TYPE'),
                    0x1A: ('name', 'PXAUTH-ID'),
                    0x1B: ('name', 'PXAUTH-PW'),
                    0x1C: ('name', 'STARTPAGE'),
                    0x1D: ('name', 'BASAUTH-ID'),
                    0x1E: ('name', 'BASAUTH-PW'),
                    0x1F: ('name', 'PUSHENABLED'),
                    0x20: ('name', 'PXADDR'),
                    0x21: ('name', 'PXADDRTYPE'),
                    0x22: ('name', 'TO-NAPID'),
                    0x23: ('name', 'PORTNBR'),
                    0x24: ('name', 'SERVICE'),
                    0x25: ('name', 'LINKSPEED'),
                    0x26: ('name', 'DNLINKSPEED'),
                    0x27: ('name', 'LOCAL-ADDR'),
                    0x28: ('name', 'LOCAL-ADDRTYPE'),
                    0x29: ('name', 'CONTEXT-ALLOW'),
                    0x2A: ('name', 'TRUST'),
                    0x2B: ('name', 'MASTER'),
                    0x2C: ('name', 'SID'),
                    0x2D: ('name', 'SOC'),
                    0x2E: ('name', 'WSP-VERSION'),
                    0x2F: ('name', 'PHYSICAL-PROXY-ID'),
                    0x30: ('name', 'CLIENT-ID'),
                    0x31: ('name', 'DELIVERY-ERR-SDU'),
                    0x32: ('name', 'DELIVERY-ORDER'),
                    0x33: ('name', 'TRAFFIC-CLASS'),
                    0x34: ('name', 'MAX-SDU-SIZE'),
                    0x35: ('name', 'MAX-BITRATE-UPLINK'),
                    0x36: ('name', 'MAX-BITRATE-DNLINK'),
                    0x37: ('name', 'RESIDUAL-BER'),
                    0x38: ('name', 'SDU-ERROR-RATIO'),
                    0x39: ('name', 'TRAFFIC-HANDL-PRIO'),
                    0x3A: ('name', 'TRANSFER-DELAY'),
                    0x3B: ('name', 'GUARANTEED-BITRATE-UPLINK'),
                    0x3C: ('name', 'GUARANTEED-BITRATE-DNLINK'),
                    0x3D: ('name', 'PXADDR-FQDN'),
                    0x3E: ('name', 'PROXY-PW'),
                    0x3F: ('name', 'PPGAUTH-TYPE'),
                    0x47: ('name', 'PULLENABLED'),
                    0x48: ('name', 'DNS-ADDR'),
                    0x49: ('name', 'MAX-NUM-RETRY'),
                    0x4A: ('name', 'FIRST-RETRY-TIMEOUT'),
                    0x4B: ('name', 'REREG-THRESHOLD'),
                    0x4C: ('name', 'T-BIT'),
                    0x4E: ('name', 'AUTH-ENTITY'),
                    0x4F: ('name', 'SPI')
                }
            )
        },

        { # Page 1
            0x06: ('characteristic', {
                    0x50: ('type', None),
                    0x53: ('type', 'PORT'),
                    0x58: ('type', 'CLIENTIDENTITY'),
                    0x55: ('type', 'APPLICATION'),
                    0x56: ('type', 'APPADDR'),
                    0x57: ('type', 'APPAUTH'),
                    0x59: ('type', 'RESOURCE')
                }
            ),

            0x07: ('parm', {
                    0x05: ('name', None),
                    0x06: ('value', lambda node, token: _values[node.attributes['name']][1][token]),
                    0x07: ('name', 'NAME'),
                    0x14: ('name', 'INTERNET'),
                    0x1C: ('name', 'STARTPAGE'),
                    0x22: ('name', 'TO-NAPID'),
                    0x23: ('name', 'PORTNBR'),
                    0x24: ('name', 'SERVICE'),
                    0x2E: ('name', 'AACCEPT'),
                    0x2F: ('name', 'AAUTHDATA'),
                    0x30: ('name', 'AAUTHLEVEL'),
                    0x31: ('name', 'AAUTHNAME'),
                    0x32: ('name', 'AAUTHSECRET'),
                    0x33: ('name', 'AAUTHTYPE'),
                    0x34: ('name', 'ADDR'),
                    0x35: ('name', 'ADDRTYPE'),
                    0x36: ('name', 'APPID'),
                    0x37: ('name', 'APROTOCOL'),
                    0x38: ('name', 'PROVIDER-ID'),
                    0x39: ('name', 'TO-PROXY'),
                    0x3A: ('name', 'URI'),
                    0x3B: ('name', 'RULE')
                }
            )
        }
    ]
}

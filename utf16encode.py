#!/usr/bin/env python

import binascii
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOWEST

def dependencies(): 
    pass

def tamper(payload, ** kwargs):

    payload = bytes(payload)
    payload = str(binascii.hexlify(payload))
    utf16_prefix = '\\u00'
    array = [payload[i:i+2] for i in range(0, len(payload), 2)]
    win = ""

    for element in array:
        win += utf16_prefix+element

    return win

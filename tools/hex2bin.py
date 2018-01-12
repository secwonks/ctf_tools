#!/usr/bin/env python

__author__ = "Wayland Morgan"
__description__ = "Decode user provided HEX string into binary data and write it to a file for analysis"
__date__ = "20171206"

hexstr = raw_input('Enter hex string: ')
filename = raw_input('Enter file name: ')
extension = ".bin"
filename = filename + extension
data = hexstr.decode('hex')
filehandle = open(filename, "wb")
filehandle.write(data)
filehandle.close()

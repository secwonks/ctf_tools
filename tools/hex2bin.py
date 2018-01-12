#!/usr/bin/env python

"""Decode user provided HEX string into binary data and write it to a file for analysis"""

__author__ = "Wayland Morgan"
__email__ = "dotwayland@gmail.com"
__date__ = "20171206"

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="Hexadecimal String")
    args = parser.parse_args()
    
    hexstr = args.input
    filename = hexstr[:12]
    extension = ".bin"
    filename = filename + extension
    data = hexstr.decode('hex')
    filehandle = open(filename, "wb")
    filehandle.write(data)
    filehandle.close()

    print "\n[*] Saved " +filename

if __name__ == '__main__':
    main()

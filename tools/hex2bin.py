#!/usr/bin/env python

import argparse

__author__ = 'Wayland Morgan'
__date__ = '20171206'
__email__ = 'dotwayland@gmail.com'
__description__ = 'Decode user provided hex string into binary data and write it to a file for analysis'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="Hexadecimal String")
    args = parser.parse_args()
    
    hexstr = args.input
    filename = hexstr[:12]+".bin"
    data = hexstr.decode('hex')
    with open(filename, "wb") as filehandle:
        filehandle.write(data)

    print "\n[*] Saved " +filename

if __name__ == '__main__':
    main()

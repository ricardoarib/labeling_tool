#!/usr/bin/python

# Converts labels with negative heights/widths to equivalent labels with positive heights/widths.
# Outputs the converted file to standard output.
#
# Version 0.1
#
# Author:
#    Ricardo Ribeiro <ribeiro@isr.ist.utl.pt>


import sys
import os
import subprocess

def main(argv):

    if len(argv) < 1 or len(argv) > 1:
        print 'usage:'
        print '       convert_negatives.py labelsfile.gt.txt'
        return

    filename = argv[0]

    f = open(filename, 'r+')

    for line in f:
        words = line.split(" ")

        frame  = int(words[0])
        x      = int(words[1])
        y      = int(words[2])
        width  = int(words[3])
        height = int(words[4])
        objectid = int(words[5])
        temp     = int(words[6])

        if width < 0 :
            x = x + width
            width = -width

        if height < 0 :
            y = y + height
            height = -height
        
        print str(frame) + " " + str(x) + " " + str(y) + " " + str(width) + " " + str(height) + " " + str(objectid) + " " + str(temp)
        
    f.close

    

if __name__ == "__main__":
   main(sys.argv[1:])


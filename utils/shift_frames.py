#!/usr/bin/python

# Shifts the labels in time (to the past or to the future).
# Outputs the converted file to standard output.
#
# Version 0.1
#
# Author:
#    Ricardo Ribeiro <ribeiro@isr.ist.utl.pt>


import sys
import os
import subprocess
import argparse

def main(argv):


    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="the file you want to convert")
    parser.add_argument("-f", "--fromframe" , type=int, help="frame number to start from", default=0 )
    parser.add_argument("-t", "--toframe"   , type=int, help="frame number to end to", default=float('inf') )
    parser.add_argument("-s", "--shift", type=int, help="shift (positive shifts to the future, negative shifts to the past.)", default=1 )
    parser.add_argument("-i", "--id", type=int, help="if specified, only shift frames for this object_ID. Otherwise, shift all objects", default=-1 )
    args = parser.parse_args()

    shift_all_ids = (args.id == -1)

    #print args
    #print args.filename
    #print args.fromframe
    #print args.toframe
    #print args.shift


    f = open(args.filename, 'r+')

    for line in f:
        words = line.split(" ")

        frame  = int(words[0])
        x      = int(words[1])
        y      = int(words[2])
        width  = int(words[3])
        height = int(words[4])
        objectid = int(words[5])
        temp     = int(words[6])


        if (frame >= args.fromframe) and (frame <= args.toframe) :
            if shift_all_ids or (objectid == args.id) :
                frame += args.shift

        print str(frame) + " " + str(x) + " " + str(y) + " " + str(width) + " " + str(height) + " " + str(objectid) + " " + str(temp)
        
    f.close

    

if __name__ == "__main__":
   main(sys.argv[1:])


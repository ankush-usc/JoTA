#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # There is location in each line, so we need to count words based on location
    # Format of the line would be - location:company:summary:date:jobtitle:joblink
    
    words = line.split('\t')
	
    
    # increase counters
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    #
    # tab-delimited; the trivial word count is 1
    # key would be location, rest all is split as key:value
    print '%s\t%s::%s::%s::%s::%s#%s' % (words[0],words[1],words[2],words[3],words[4],words[5], 1)

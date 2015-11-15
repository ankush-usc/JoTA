#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    jobs = line.split('##')
    for job in jobs:
        skills = job.split('::')
        skill = skills[2].split(',')
        for s in skill:
            s = s.strip()
            print '%s\t%s#%s' % (s,job,1)



    

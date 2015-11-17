__author__ = 'divyaindi'
#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.split('\t')
    count = line[2]
    jobs = line[1].split('##')
    for job in jobs:
        skills = job.split('::')
        skill = skills[2].split(',')
        for s in skill:
            s = s.strip()
            print '%s\t%s::%s#%s' % (s,job,count,1)



    
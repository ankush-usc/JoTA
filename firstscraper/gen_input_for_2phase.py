import os
import sys
import glob


path = sys.argv[1];

dest = open('input2skill.txt','w')

for filename in glob.glob(os.path.join(path, 'part*')):
    src = open(filename,'r')

    for line in src:
    	dest.write(line)

    src.close()
dest.close()
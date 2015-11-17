import os
import sys
import glob


path = sys.argv[1];
field = sys.argv[2];

if (field == "location"):
	dest = open('locMergeFile.tsv','w')
	dest.write("location	location_value	count\n")
else:
	dest = open('skillMergeFile.tsv','w')
	dest.write("skill	skill_value	count");
    	
for filename in glob.glob(os.path.join(path, 'part*')):
    print filename
    src = open(filename,'r')

    for line in src:
    	dest.write(line)
    	
    src.close()
dest.close()

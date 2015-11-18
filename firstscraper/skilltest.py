import sys
     
# go through the input file, one line at a time
for line in sys.stdin:   
    line = line.strip()   
    skill_key_array = line.split('\t')
    skill_value_array = skill_key_array[1].split('##') 
    location_key_array= skill_key_array[1].split('::')
    print '%s:%s::%s:%s'% (skill_key_array[0],skill_key_array[2],location_key_array[0],location_key_array[len(location_key_array)-1])  

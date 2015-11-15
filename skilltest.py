skill = {}        # dictionary
infile = open('skill_input.txt')      # open the file for reading

for line in infile:      # go through the input file, one line at a time
    line = line.strip()     # remove the newline character at the end
    skill_key_array = line.split('\t')# split up line around tab character
    skill_value_array=skill_key_array[1].split('##') #split up around ## character
    location_key_array= skill_key_array[1].split('::')
    print '%s:%s::%s:%s'% (skill_key_array[0],skill_key_array[2],location_key_array[0],location_key_array[5])  

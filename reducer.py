#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
current_key_string = None

# input comes from STDIN
# line format = Sunnyvale	NetApp::C, file systems::Jun 12::MTS3::<link>#1
# (Location<tab>company::skills::date::MTS3::link#value

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    # priliminary split text to key and value
    initial_key_array = line.split('\t'); 
    initial_value_array = initial_key_array[1].split('#');
    # convert count (currently a string) to int
    try:
        count = int(initial_value_array[1])
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    word = initial_key_array[0]
    key_string = initial_value_array[0]

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
        current_key_string = str(current_key_string) + "##" + initial_value_array[0]

    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_word,current_key_string,current_count)
        current_count = count
        current_word = word
	current_key_string = key_string

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s\t%s' % (current_word,current_key_string, current_count)
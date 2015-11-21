#!/usr/bin/env python

import sys

last_key      = None
running_total = 0
channel       = []

for input_line in sys.stdin:
    
    input_line = input_line.strip()
    this_key, value = input_line.split("\t", 1)

    try:
        value = int(value)
    except:
        channel.append(value)
        value = 0
 
    if last_key == this_key:
        running_total += value
    else:
        if last_key and 'ABC' in channel:
            print '{0}\t{1}'.format(last_key, running_total)
        
	running_total = value
        last_key = this_key

if last_key == this_key and 'ABC' in channel:
    print '{0}\t{1}'.format(last_key, running_total)

# Debug reducer in offline mode at UNIX command line:
# cat data_gen*.txt | ./join_mapper.py | sort | ./join_reducer.py

#!/usr/bin/env python

"""
Reads key-value pairs from stdin and returns a total count for each word: < word    count >.
"""

import sys

last_key      = None                             # initialise variables
running_total = 0

for input_line in sys.stdin:
    
    input_line = input_line.strip()
    this_key, value = input_line.split("\t", 1)  # split tab-delimited key-value pairs (Hadoop default) and store in two variables
    value = int(value)
    
    if last_key == this_key:                     # if this_key is equal to last_key
        running_total += value                   # add its value to running_total
    else:					 # else print key-value pair
        if last_key:
            print '{0}\t{1}'.format(last_key, running_total)
        
	running_total = value                    # reset values
        last_key = this_key

if last_key == this_key:
    print '{0}\t{1}'.format(last_key, running_total)

# Debug reducer in offline mode at UNIX command line:
# cat testfile1 | ./wordcount_mapper.py | sort | ./wordcount_reducer.py

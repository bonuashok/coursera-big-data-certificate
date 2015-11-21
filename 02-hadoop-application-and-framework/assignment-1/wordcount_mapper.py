#!/usr/bin/env python

"""
Reads input from stdin and returns a key-value pair for each word: < word    1 >.
"""

import sys

for line in sys.stdin:                      # iterate through each line streamed from stdin
    line = line.strip()                     # strip carriage return (default)
    keys = line.split()                     # split line at spaces (default) and return a list of keys
    for key in keys:                        # iterate through keys
        value = 1        
        print '{0}\t{1}'.format(key, value) # format key-value pair as tab-delimited

# Debug mapper in offline mode at UNIX command line:
# cat testfile1 | ./wordcount_mapper.py | sort

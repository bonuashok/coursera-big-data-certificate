#!/usr/bin/env python   

import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split(',')
    print '{0}\t{1}'.format(keys[0], keys[1])

# Debug mapper in offline mode at UNIX command line:
# cat data_gen*.txt | ./join_mapper.py | sort

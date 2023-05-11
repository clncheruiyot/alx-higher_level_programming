#!/usr/bin/python3
 """Print addition of all the arguments."""
from sys import argv
add = 0
for s in argv[1:]:
    add += int(s)
print("{:d}".format(add))

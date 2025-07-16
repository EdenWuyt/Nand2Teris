# For the comparison of two .hack files (with only machine code)
# Two files must be exactly the same, inluding where to add a new line.

import sys

with open(sys.argv[1]) as f1:
    add = f1.readlines()

with open(sys.argv[2]) as f2:
    example = f2.readlines()

for i in range(len(add)):
    assert add[i] == example[i], f'{add[i], example[i]}'

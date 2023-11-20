#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if s[0].islower():
        c = s[0].capitalize()
        s = c+s[1:]
    for i in range(1,len(s)):
        if s[i-1] == ' ':
            if s[i].islower():
                c = s[i].capitalize()
                s = s[:i]+c+s[i+1:]
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

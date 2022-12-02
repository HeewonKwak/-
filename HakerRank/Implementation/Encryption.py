#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    n = math.trunc(math.sqrt(len(s)))
    if pow(n,2) == len(s):
        m = n
    elif n * n+1 < len(s):
        m = n+1
        n += 1
    else:
        m = n + 1
    ans = ""
    for i in range(m):
        for j in range(n):
            if len(s) > (m)*j+i:
                ans += s[(m)*j+i]
        ans += " "
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

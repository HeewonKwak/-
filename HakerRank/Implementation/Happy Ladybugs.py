# https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    if len(b) == 1 and b[0] != '_':
        return 'NO'
    if '_' not in b:
        cnt = 0
        check = b[0]
        for idx, i in enumerate(b):
            if check == i:
                cnt += 1
            else:
                if cnt == 1 or (idx == len(b) - 1):
                    return 'NO'
                cnt = 1
                check = i
        return 'YES'
    elif 1 in Counter(b.replace('_', '')).values():
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

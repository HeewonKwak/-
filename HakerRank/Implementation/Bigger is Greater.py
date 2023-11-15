# https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    if sorted(w, reverse=True) == list(w):
        return 'no answer'
    ans = ''
    check = 0
    big_alps = []
    for i, alp in enumerate(reversed(list(w))):
        if alp <= w[-(i + 2)]:
            continue
        ww = list(w[-(i+2):])
        for k in ww:
            if w[-(i + 2)] < k:
                big_alps.append(k)
        ans += min(big_alps)
        ww.remove(min(big_alps))
        for j in sorted(ww):
            ans += j
        check = i
        break
    ans = w[:-(check+2)] + ans
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

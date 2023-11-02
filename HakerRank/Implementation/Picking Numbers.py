# https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from collections import Counter

def pickingNumbers(a):
    # Write your code here
    cc = Counter(a)
    kk = sorted(list(cc.keys()))
    ans = 0
    for i in range(len(cc.keys())-1):
        if kk[i+1] - kk[i] == 1:
            ans = max(ans, cc[kk[i]] + cc[kk[i + 1]])
        else:
            ans = max(ans, cc[kk[i]])
    ans = max(ans, cc[kk[-1]])
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

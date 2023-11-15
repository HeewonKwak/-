# https://www.hackerrank.com/challenges/the-power-sum/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N):
    # Write your code here
    ans = 0
    n = int(math.pow(X, 1/N))
    nums = []
    for i in range(1, n+1):
        nums.append(math.pow(i, N))
    ans = getSum(nums, X, 0, 0)
    return ans
    
def getSum(nums, X, idx, ss):
    # print(ss, idx)
    if int(ss) > X:
        return 0
    elif ss == X:
        print('idx')
        return 1
    elif idx == len(nums):
        return 0
    else:
        return getSum(nums, X, idx + 1, ss) + getSum(nums, X, idx + 1, ss+nums[idx])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    alp = list(set(s))
    alp.sort()
    alp_num = []
    alp_cnt = []
    ans = []
    for i in alp:
        alp_num.append(ord(i)-96)
        ss = ""
        ssl = 0
        maxl = 0
        for j in range(len(s)):
            if s[j] == i:
                ssl += 1
                maxl = max(maxl, ssl)
            else:
                ssl = 0
        alp_cnt.append(maxl)
    for i in queries:
        for j in range(len(alp)):
            if i % alp_num[j] == 0 and i <= alp_num[j] * alp_cnt[j]:
                ans.append("Yes")
                break
            elif j == len(alp)-1:
                ans.append("No")
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

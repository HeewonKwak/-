# https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    max_val = 0
    cnt = 0
    for a, b in combinations(topic, 2):
        if bin_check(a, b) > max_val:
            max_val = bin_check(a, b)
            cnt = 1
        elif bin_check(a, b) == max_val:
            cnt += 1
    return [max_val, cnt]
        
def bin_check(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != '0' or b[i] != '0':
            cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

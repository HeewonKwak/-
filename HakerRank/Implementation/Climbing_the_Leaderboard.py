#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ans = [0 for _ in range(len(player))]
    if len(ranked) == 1:
        for i, j in enumerate(player):
            if j < ranked[0]:
                ans[i] = 2
            else:
                ans[i] = 1
        return ans
    ranked = list(set(ranked))
    ranked.sort()
    start_idx = 0
    for i, j in enumerate(player):
        for k in range(start_idx, len(ranked) - 1):
            if ranked[k] <= j < ranked[k+1]:
                ans[i] = len(ranked) - k
                start_idx = k
                break
            elif j < ranked[k]:
                ans[i] = len(ranked) - k + 1
                start_idx = k
                break
            elif k == len(ranked) -2 and j >= ranked[k+1]:
                ans[i] = 1
                start_idx = k
                break
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
# https://www.hackerrank.com/challenges/flatland-space-stations/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
# def flatlandSpaceStations(n, c):
#     if n == len(c):
#         return 0
#     citys = [i for i in range(n) if i not in c]
#     distances = [0]
#     for city in citys:
#         distance = []
#         for station in c:
#             if abs(city-station) == 1:
#                 distance = [1]
#                 break
#             distance.append(abs(city-station))
#         distances.append(min(distance))

#     return max(distances)
    
def flatlandSpaceStations(n, c):
    if n == len(c):
        return 0
    
    c.sort()
    
    max_distance = 0
    for i in range(1, len(c)):
        max_distance = max(max_distance, (c[i] - c[i-1]) // 2)
    
    max_distance = max(max_distance, c[0], n-1 - c[-1])
    
    return max_distance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

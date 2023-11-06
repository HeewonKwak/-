# Sorting / Insertion Sort - Part 1
# https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    idx = n - 1
    sort_arr = sorted(arr)
    save = False
    while(1):
        if arr[idx - 1] > arr[idx]:
            if save is False:
                save = arr[idx]
            arr[idx] = arr[idx - 1]
        elif arr[idx - 1] <= arr[idx]:
            if save is not False:
                if save < arr[idx - 1]:
                    arr[idx] = arr[idx - 1]
                else:
                    arr[idx] = save
                    save = False
        idx -= 1
        if save is not False and idx == -1:
            arr[0] = save
        print(" ".join(map(str, arr)))
        if sort_arr == arr:
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

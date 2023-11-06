# Sorting / Insertion Sort - Part 2
# https://www.hackerrank.com/challenges/insertionsort2/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(arr):
    # Write your code here
    idx = len(arr) - 1
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
        if sort_arr == arr:
            break
    return arr

def insertionSort2(n, arr):
    # Write your code here
    array = arr.copy()
    for i in range(2,n+1):
        array = insertionSort1(array[:i]) + array[i:]
        print(" ".join(map(str, array)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

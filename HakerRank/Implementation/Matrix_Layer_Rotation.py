#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#
def printmatrix(m, matrix):
    for i in range(m):
        for j in matrix[i]:
            print(j, end=' ')
        print('')


def matrixRotation(m, n, matrix, r):
    # Write your code here
    check = 2*n + 2*m - 4

    mat = matrix
    i = 0
    while(check > 0 and i < min(n, m)//2):
        times = r % check
        for _ in range(times):
            a = mat[i][i]
            b = mat[m-1-i][i]
            c = mat[m-1-i][n-1-i]
            d = mat[i][n-1-i]
            for j in range(1,n-2*i):
                mat[i][j+i-1] = mat[i][j+i]
            for j in range(n-2*i-1,0,-1):
                mat[m-i-1][j+i] = mat[m-i-1][j+i-1]
            for j in range(m-1-2*i-1,0,-1):
                mat[i+j+1][i] = mat[i+j][i]
            for j in range(1,m-1-2*i):
                mat[i+j-1][n-1-i] = mat[i+j][n-1-i]
            mat[i+1][i] = a
            mat[m-1-i][i+1] = b
            mat[m-2-i][n-1-i] = c
            mat[i][n-2-i] = d

        i += 1
        check -= 8

    printmatrix(m, mat)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(m, n, matrix, r)
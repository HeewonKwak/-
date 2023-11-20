# https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

# def bomberMan(n, grid):
#     # Write your code here
#     grid = [[1 if i == 'O' else 0 for i in g] for g in grid]
#     for _ in range(n):
#         # grid = now_grid
#         check = 0
#         for x in range(len(grid)):
#             for y in range(len(grid[0])):
#                 if grid[x][y] == 1:
#                     grid[x][y] += 1
#                 elif grid[x][y] == 2:
#                     check = 1
#                     grid[x][y] += 1
#                 elif grid[x][y] == 3:
#                     if x >= 1 and grid[x-1][y] < 3:
#                         grid[x-1][y] = 4
#                     if y >= 1 and grid[x][y-1] < 3:
#                         grid[x][y-1] = 4
#                     if x <= len(grid) - 2 and grid[x+1][y] < 3:
#                         grid[x+1][y] = 4
#                     if y <= len(grid[0]) - 2 and grid[x][y+1] < 3:
#                         grid[x][y+1] = 4
#                     grid[x][y] = 4
#         if check == 1:
#             for x in range(len(grid)):
#                 for y in range(len(grid[0])):
#                     if grid[x][y] == 0:
#                         grid[x][y] = 1
#         for x in range(len(grid)):
#             for y in range(len(grid[0])):
#                 if grid[x][y] == 4:
#                     grid[x][y] = 0
#         # print([''.join('.' if i == 0 else 'O' for i in g) for g in grid])
#     final_grid = [''.join('.' if i == 0 else 'O' for i in g) for g in grid]
    
#     return final_grid

def bomberMan(n, grid):
    # Write your code here
    if n == 1:
        return grid
    if n % 2 == 0:
        return ['O'*len(grid[0]) for _ in grid]
    grid = [[1 if i == 'O' else 0 for i in g] for g in grid]
    for _ in range((n//2 + 1)% 2 + 1):
        xy = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    xy.append([x, y])
        grid = [[1 for _ in range(len(grid[0]))] for _ in grid]
        for x, y in xy:
            grid = bomb(grid, x, y)
        
    return [''.join('.' if i == 0 else 'O' for i in g) for g in grid]
    
def bomb(grid, x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            grid[nx][ny] = 0
    grid[x][y] = 0
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

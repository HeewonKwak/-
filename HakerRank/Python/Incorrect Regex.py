# Python / Errors and Exceptions / Incorrect Regex
# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
# ONLY WORK PYPY
import re
n = int(input())
for _ in range(n):
    reg = input()
    try:
        re.compile(reg)
        print('True')
    except re.error:
        print('False')
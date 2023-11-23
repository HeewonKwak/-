# Python / Regex and Parsing / Detect Floating Point Number
# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(n):
    num = input()
    if not re.search(r'^[^.]*\.[^.]*$', num):
        print('False')
    elif re.search(r'[a-zA-Z]', num):
        print('False')
    elif re.search(r'[^\.|\+|\-|\d]', num):
        print('False')
    elif re.search(r'\-\+|\+\-', num):
        print('False')
    elif re.search(r'[\+\-]', num) and not re.search(r'^\-|^\+', num):
        print('False')
    else:
        print('True')
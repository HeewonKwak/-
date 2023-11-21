# Python / Collections / Collections.namedtuple()
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
Average = namedtuple('average', input().split())
_sum = 0
for _ in range(n):
    a, b, c, d = input().split()
    x = Average(a, b, c, d)
    _sum += int(x.MARKS)
print(_sum / n)

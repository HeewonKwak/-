# Python / Collections / Word Order
# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
order = OrderedDict()
for _ in range(n):
    word = input()
    if word in order.keys():
        order[word] += 1
    else:
        order[word] = 1
print(len(order))
print(*order.values())
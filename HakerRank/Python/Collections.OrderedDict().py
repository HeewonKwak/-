# Python / Collections / Collections.OrderedDict()
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict, defaultdict
n = int(input())
ordered_dictionary = OrderedDict()
ordered_cnt = defaultdict(int)
for _ in range(n):
    order = input().split()
    mm = order[0]
    if len(order[:-1]) > 1:
        mm = ' '.join(order[:-1])
    ordered_dictionary[mm] = order[-1]
    ordered_cnt[mm] += 1
for menu, cnt in ordered_dictionary.items():
    print(menu, int(cnt) * int(ordered_cnt[menu]))
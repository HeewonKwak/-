# https://www.hackerrank.com/challenges/jim-and-the-orders/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Write your code here
    order_dict = defaultdict(int)
    for idx, [order, prep] in enumerate(orders):
        order_dict[idx+1] = order + prep
    ans = []
    for i, _ in sorted(order_dict.items(), key=lambda x:x[1]):
        ans.append(i)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

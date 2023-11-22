# Python / Collections / Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

if __name__ == '__main__':
    s = input()
    alp = defaultdict(int)
    for i in s:
        alp[i] += 1
    for i, j in sorted(alp.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(i, j)
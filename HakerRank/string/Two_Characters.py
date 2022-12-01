#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    
    alp = list(set(list(s)))
    
    if len(alp) == 1:
        return 0
    
    ans = []
    check = ""
    b = ""
    
    for i in range(len(alp)-1):
        for j in range(i+1, len(alp)):
            for k in s:
                if k == alp[i] or k==alp[j]:
                    b += k
            
            for kk, k in enumerate(b):
                if k == check:
                    ans.append(0)
                    break
                elif kk == len(b)-1:
                    print(b)
                    print(ans)
                    ans.append(len(b))
                check = k
            check = ""
            b = ""
            
    return max(ans)
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()

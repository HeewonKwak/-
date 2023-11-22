# Python / Collections / Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
t = int(input())
for _ in range(t):
    n = int(input())
    nums = deque(map(int, input().split()))
    sidelength = pow(2, 31)
    for _ in range(len(nums)):
        if nums[0] >= nums[-1] and sidelength >= nums[0]:
            sidelength = nums.popleft()
        elif nums[0] < nums[-1] and sidelength >= nums[-1]:
            sidelength = nums.pop()
        else:
            print('No')
            break
    else:
        print('Yes')
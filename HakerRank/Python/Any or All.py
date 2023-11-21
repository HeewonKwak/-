# Python / Built-Ins / Any or All
# https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nums = list(map(int,input().split()))
print((all([True if i > 0 else False for i in nums])) and any([True if str(i) == str(i)[::-1] else False for i in nums]))
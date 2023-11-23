# Python / Python Functionals / Map and Lambda Function
# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    nums = [0 for _ in range(n)]
    nums[1] = 1
    for i in range(2, n):
        nums[i] = nums[i-1] + nums[i-2]
    return nums

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
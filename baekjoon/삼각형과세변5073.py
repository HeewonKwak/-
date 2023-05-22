# 문제
while(1):
    a, b, c = map(int, input().split())
    max_num = max(a, b, c)
    if max_num ==0:
        break
    if max_num >= a + b + c - max_num:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a==b or b==c or c==a:
        print('Isosceles')
    else:
        print('Scalene')
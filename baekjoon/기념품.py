n = int(input())

people = [i for i in range(1, n+1)]

count = 1

while(1):
    if len(people) == 1:
        break
    a = pow(count, 3)
    b = a % len(people)
    if b == 0:
        b = len(people)
    people = people[b:] + people[:b-1] 
    count += 1
    
print(people[0])
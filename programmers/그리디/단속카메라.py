# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 1
    routes.sort(key = lambda x : (x[1], x[0]))
    ff = routes[0][1]
    for i in routes:
        if i[0] > ff:
            answer += 1
            ff = i[1]
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
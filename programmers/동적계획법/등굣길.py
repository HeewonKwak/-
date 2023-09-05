# https://school.programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    graph = [[0 for _ in range(n+1)] for _ in range(m+1)]
    graph[1][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if j < n and [i, j+1] not in puddles:
                graph[i][j+1] += graph[i][j]
            if i < m and [i+1, j] not in puddles:
                graph[i+1][j] += graph[i][j]
    print(graph)
    return graph[-1][-1] % 1000000007
# https://school.programmers.co.kr/learn/courses/30/lessons/154538
def solution(x, y, n):
    answer = 0
    dp = [float('INF')] * (y*3 + 1)
    dp[x] = 0
    for i in range(x, y):
        if dp[i] != float('INF'):
            dp[i+n] = min(dp[i] + 1, dp[i+n])
            dp[i*2] = min(dp[i] + 1, dp[i*2])
            dp[i*3] = min(dp[i] + 1, dp[i*3])
    if dp[y] == float('INF'):
        return -1
    return dp[y]
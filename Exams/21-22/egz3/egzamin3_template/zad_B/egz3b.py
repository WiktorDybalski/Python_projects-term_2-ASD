from egz3btesty import runtests


def maze(L):
    if L[0][0] == '#':
        return -1
    inf = float("inf")
    n = len(L)
    dp = [[-inf for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0
    for i in range(1, n):
        if L[i][0] == '#':
            break
        dp[i][0] = dp[i - 1][0] + 1
    for j in range(1, n):
        temp = -inf
        for i in range(n):
            if L[i][j] == '#':
                temp = -inf
            else:
                temp = max(temp, dp[i][j - 1])
                temp += 1
                dp[i][j] = max(dp[i][j], temp)
        temp = -inf
        for i in reversed(range(n)):
            if L[i][j] == '#':
                temp = -inf
            else:
                temp = max(temp, dp[i][j - 1])
                temp += 1
                dp[i][j] = max(dp[i][j], temp)
    if dp[n - 1][n - 1] < 0:
        return -1
    return dp[n - 1][n - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)

from zad8ktesty import runtests


def napraw(s, t):
    ns = len(s)
    nt = len(t)
    dp = [[float('inf') for _ in range(ns + 1)] for _ in range(nt + 1)]
    for i in range(nt + 1):
        dp[i][0] = i
    for j in range(1, ns + 1):
        dp[0][j] = j
    for i in range(1, nt + 1):
        for j in range(1, ns + 1):
            if s[j - 1] == t[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[nt][ns]


runtests(napraw)

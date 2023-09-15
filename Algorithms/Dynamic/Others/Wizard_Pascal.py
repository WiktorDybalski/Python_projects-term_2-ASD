from math import inf

P = 4
T = [(1, 0, 2), (2, -1, 1), (1, 0, 3)]


def f(T, prefix_sum_T, dp, t, s):
    if dp[t][s] != -inf:
        return dp[t][s]
    n = len(T)
    for i in range(n):
        dp[t][s] = max(dp[t][s], f(T, prefix_sum_T, dp, t - i, s - 1) + prefix_sum_T[s][i])
    return dp[s][t]


def pascal(T, plates):
    k = len(T[0])
    stacks = len(T)
    dp = [[-inf for _ in range(k)] for _ in range(plates)]
    prefix_sum_T = [[0 for _ in range(k)] for _ in range(stacks)]
    for i in range(stacks):
        for j in range(k):
            if j == 0:
                prefix_sum_T[i][j] = T[i][j]
            else:
                prefix_sum_T[i][j] = prefix_sum_T[i][j - 1] + T[i][j]
    for i in range(plates):
        if i >= k:
            dp[i][0] = prefix_sum_T[0][k - 1]
        else:
            dp[i][0] = prefix_sum_T[0][i]
    for i in range(1, k):
        if T[i][0] > dp[0][i - 1]:
            dp[0][i] = T[i][0]
        else:
            dp[0][i] = dp[0][i - 1]
    the_most_b = f(T, prefix_sum_T, dp, plates - 1, k - 1)
    return the_most_b


print(pascal(T, P))

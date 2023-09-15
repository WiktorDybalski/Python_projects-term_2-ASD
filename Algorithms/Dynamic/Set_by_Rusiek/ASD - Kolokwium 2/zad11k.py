from zad11ktesty import runtests


def dyn(T, dp, i, p1_sum, p2_sum):
    if i == len(T):
        dp[i][p1_sum] = abs(p1_sum - p2_sum)
        return dp[i][p1_sum]

    if dp[i][p1_sum] != float('inf'):
        return dp[i][p1_sum]

    dp[i][p1_sum] = min(dyn(T, dp, i + 1, p1_sum + T[i], p2_sum), dyn(T, dp, i + 1, p1_sum, p2_sum + T[i]))
    return dp[i][p1_sum]


def kontenerowiec(T):
    n = len(T)
    total_sum = sum(T)
    dp = [[float('inf') for _ in range(total_sum + 1)] for _ in range(n + 1)]
    the_lowest = dyn(T, dp, 0, 0, 0)
    return the_lowest


runtests(kontenerowiec)

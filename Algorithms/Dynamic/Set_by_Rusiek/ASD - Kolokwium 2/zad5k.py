from zad5ktesty import runtests


def dyn(A, dp, a, b):
    if dp[a][b] != 0:
        return dp[a][b]

    if a == b:
        dp[a][b] = (A[a], 0)
    elif a + 1 == b:
        dp[a][b] = (max(A[a], A[b]), min(A[a], A[b]))
    else:
        if A[a] + dyn(A, dp, a + 1, b)[1] > A[b] + dyn(A, dp, a, b - 1)[1]:
            dp[a][b] = (A[a] + dyn(A, dp, a + 1, b)[1], dyn(A, dp, a + 1, b)[0])
        else:
            dp[a][b] = (A[b] + dyn(A, dp, a, b - 1)[1], dyn(A, dp, a, b - 1)[0])

    return dp[a][b]


def garek(A):
    n = len(A)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    the_best = dyn(A, dp, 0, n - 1)
    return the_best[0]


runtests(garek)

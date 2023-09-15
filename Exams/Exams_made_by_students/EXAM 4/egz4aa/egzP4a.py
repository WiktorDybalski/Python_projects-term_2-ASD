from egzP4atesty import runtests


def lis(T, dp, i):
    inf = float('inf')
    if i == 0:
        return 1
    if dp[i] != -inf:
        return dp[i]
    maxx = 1
    for j in range(i):
        if T[j] <= T[i]:
            maxx = max(maxx, lis(T, dp, j) + 1)
    dp[i] = maxx
    return dp[i]


def mosty(T):
    inf = float('inf')
    T = sorted(T, key=lambda x: (x[0], x[1]))
    n = len(T)
    new_T = [T[i][1] for i in range(n)]
    new_T.append(inf)
    n = len(new_T)
    dp = [-inf for _ in range(n)]
    output = lis(new_T, dp, n - 1)
    return output - 1


runtests(mosty, all_tests=True)

from zad7ktesty import runtests


def partition(A, B, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            B[i], B[j] = B[j], B[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    B[i + 1], B[r] = B[r], B[i + 1]
    return i + 1


def quick_sort(A, B, p, r):
    while p < r:
        q = partition(A, B, p, r)
        quick_sort(A, B, p, q - 1)
        p = q + 1
    return A, B


def explore(T, y, x, visited, sum):
    ny = len(T)
    nx = len(T[0])
    if y >= ny or y < 0 or x >= nx or x < 0:
        return 0
    if visited[y][x] or T[y][x] == 0:
        return 0
    visited[y][x] = True
    sum += T[y][x] + explore(T, y + 1, x, visited, sum) + explore(T, y, x + 1, visited, sum) + \
           explore(T, y, x - 1, visited, sum) + explore(T, y - 1, x, visited, sum)
    return sum


def dyn(costs, Z, l):
    n = len(costs)
    dp = [[0 for _ in range(l + 1)] for _ in range(n)]
    for i in range(costs[0], l + 1):
        dp[0][i] = Z[0]
    for j in range(costs[0], l + 1):
        for i in range(1, n):
            dp[i][j] = dp[i - 1][j]
            if j - costs[i] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - costs[i]] + Z[i])
    return dp[n - 1][l]


def ogrodnik(T, D, Z, l):
    n = len(D)
    nTy = len(T)
    nTx = len(T[0])
    costs = [0] * n
    visited = [[False for _ in range(nTx)] for _ in range(nTy)]
    for i in range(n):
        costs[i] = explore(T, 0, D[i], visited, sum)
    costs, Z = quick_sort(costs, Z, 0, n - 1)
    max_profit = dyn(costs, Z, l)
    return max_profit


runtests(ogrodnik, all_tests=True)

from egzP5atesty import runtests


# Complexity: O(n)
def getMaxArea(T):
    s = [-1, 0]
    n = len(T)
    area = 0
    ls = [-1 for _ in range(n)]
    rs = [n for _ in range(n)]
    for i in range(1, n):
        while s[len(s) - 1] != -1 and T[s[len(s) - 1]] > T[i]:
            rs[s[len(s) - 1]] = i
            s.pop()
        if T[i] == T[i - 1]:
            ls[i] = ls[i - 1]
        else:
            ls[i] = s[len(s) - 1]
        s.append(i)
    for j in range(0, n):
        area = max(area, T[j] * (rs[j] - ls[j] - 1))

    return area


def inwestor(T):
    return getMaxArea(T)


# Complexity: O(n^2)
# def f(T, dp, a, b):
#     if a == b:
#         return T[a]
#     if dp[a][b] != -1:
#         return dp[a][b]
#     dp[a][b] = min(f(T, dp, a, b - 1), T[b])
#     return dp[a][b]
#
#
# def inwestor(T):
#     maxx = 0
#     n = len(T)
#     dp = [[-1 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(i, n):
#             maxx = max(maxx, (j - i + 1) * f(T, dp, i, j))
#     return maxx


# Complexity: O(n^3)
# def inwestor(T):
#     the_biggest = 0
#     n = len(T)
#     dp = [[0 for _ in range(2)] for _ in range(n)]
#     for i in range(n - 1):
#         for j in range(i + 1, n + 1):
#             total = 1
#             temp = T[i:j]
#             n_temp = j - i
#             the_lowest = min(temp)
#             total *= the_lowest * n_temp
#             if dp[i][1] < total:
#                 dp[i][0] = the_lowest
#                 dp[i][1] = total
#         the_biggest = max(the_biggest, dp[i][1])
#     return the_biggest


runtests(inwestor, all_tests=False)

from bisect import bisect_right

from egzP8atesty import runtests


def reklamy(T, S, o):
    inf = float('inf')
    n = len(S)
    for i in range(n):
        T[i] = (T[i][0], T[i][1], S[i])
    T.append((inf, inf, 0))
    T = sorted(T, key=lambda x: x[0])
    result = 0

    M = [0 for _ in range(n)]
    M[n - 1] = T[n - 1][2]

    for i in range(n - 2, -1, -1):
        M[i] = max(M[i + 1], T[i][2])
    S = [T[i][0] for i in range(n)]
    for i in range(n):
        end = T[i][1]
        idx = bisect_right(S, end, lo=i + 1)
        second = 0
        if idx < n and S[idx] != end:
            second = M[idx]
        result = max(result, T[i][2] + second)
    return result


# Complexity: O(n^2)
# def reklamy(T, S, o):
#     inf = float('inf')
#     n = len(S)
#     for i in range(n):
#         T[i] = (T[i][0], T[i][1], S[i])
#     T.append((inf, inf, 0))
#     maxx = 0
#     T = sorted(T, key=lambda x: x[0])
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             if T[i][1] < T[j][0]:
#                 maxx = max(maxx, T[i][2] + T[j][2])
#     return maxx


runtests(reklamy, all_tests=True)

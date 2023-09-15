from math import inf

# The algorythm return the biggest sum of the things that the theft can steal considering that he can not
# steal things next to each other.

T = [3, 5, 2, 4, 2, 3, 2, 6, 2, 1, 6]


def f(T, dp, i):
    if i == 0:
        return T[i]
    if i == 1:
        return T[i]
    if dp[i] != -inf:
        return dp[i]
    val = max(f(T, dp, i - 1), f(T, dp, i - 2) + T[i])
    dp[i] = val
    return val


def thieft(T):
    n = len(T)
    dp = [-inf for _ in range(n)]
    result = f(T, dp, n - 1)
    return result


print(thieft(T))

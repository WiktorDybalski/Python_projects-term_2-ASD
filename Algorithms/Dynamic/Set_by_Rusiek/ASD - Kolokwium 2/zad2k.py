from zad2ktesty import runtests


def palindrom(S):
    n = len(S)
    if n < 2:
        return S

    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    start = 0
    max_len = 1

    for i in range(n - 1):
        if S[i] == S[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    for curr_len in range(3, n + 1):
        for i in range(n - curr_len + 1):
            j = i + curr_len - 1
            if S[i] == S[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = curr_len

    return S[start:start + max_len]


runtests(palindrom)

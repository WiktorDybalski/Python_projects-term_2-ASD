from math import sqrt, floor

from zad10ktesty import runtests


def dywany(N):
    dp = [float('inf') for _ in range(N + 1)]
    numbers = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        if i * i <= N:
            dp[i * i] = 1
            numbers[i * i].append(i * i)
        else:
            break
    for i in range(2, N + 1):
        for k in range(i - 1, 0, -1):
            if dp[k] + dp[i - k] < dp[i]:
                dp[i] = dp[k] + dp[i - k]
                numbers[i] = numbers[k] + numbers[i - k]
    for i in range(0, len(numbers[N])):
        numbers[N][i] = int(sqrt(numbers[N][i]))
    return numbers[N][::-1]


runtests(dywany)

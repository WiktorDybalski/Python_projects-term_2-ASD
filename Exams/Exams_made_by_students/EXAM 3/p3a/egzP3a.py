from egzP3atesty import runtests
from math import inf


class Node:
    def __init__(self, wyborcy, koszt, fundusze):
        self.next = None
        self.wyborcy = wyborcy
        self.koszt = koszt
        self.fundusze = fundusze
        self.x = None


def cnt_people(constituency, n, p):
    dp = [[0 for _ in range(p + 1)] for _ in range(n)]
    for i in range(constituency[0][1], p + 1):
        dp[0][i] = constituency[0][0]
    for j in range(1, p + 1):
        for i in range(1, n):
            dp[i][j] = dp[i - 1][j]
            if j - constituency[i][1] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - constituency[i][1]] + constituency[i][0])
    return dp[n - 1][p]


def wybory(T):
    n = len(T)
    info = [[] for _ in range(n)]
    for i in range(n):
        okr = T[i]
        info[i].append((okr.wyborcy, okr.koszt, okr.fundusze))
        while okr.next is not None:
            okr = okr.next
            info[i].append((okr.wyborcy, okr.koszt, okr.fundusze))
        info[i].sort(key=lambda x: x[1])
    cnt = 0
    for i in range(n):
        n = len(info[i])
        p = info[i][0][2]
        cnt += cnt_people(info[i], n, p)
    return cnt


runtests(wybory, all_tests=True)

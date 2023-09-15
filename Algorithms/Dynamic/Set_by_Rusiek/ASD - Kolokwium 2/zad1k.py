from zad1ktesty import runtests


def roznica(S):
    print(S)
    if not '0' in S:
        return -1
    n = len(S)
    Mem = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for c in range(n):
        if S[c] == '1':
            Mem[c][c + 1] = -1
        else:
            Mem[c][c + 1] = 1
    max_cnt = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if S[j - 1] == '1':
                Mem[i][j] = Mem[i][j - 1] - 1
            else:
                Mem[i][j] = Mem[i][j - 1] + 1
            max_cnt = max(Mem[i][j], max_cnt)
    return max_cnt


runtests(roznica)

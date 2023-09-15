# The algorythm return the minimal amount of machines needed to cover every plot

k = 3
F = [True, False, True, True, False, False, True, False]


def min_machines(F, k):
    n = len(F)
    index = 0
    cnt = 0
    cover = [0 for _ in range(n)]
    for i in range(k - 1, -1, -1):
        if F[i]:
            index = i
            cnt += 1
            break
    cover[index] += 1
    for i in range(1, k):
        if index + i <= n - 1:
            cover[index + i] += 1
        if index - i >= 0:
            cover[index - i] += 1
    i = index + k
    while i <= n - 1:
        for j in range(k - 1, -1, -1):
            if i + j > n - 1:
                continue
            if F[i + j]:
                cnt += 1
                cover[i + j] += 1
                for c in range(1, k):
                    if i + j + c <= n - 1:
                        cover[i + j + c] += 1
                    if i + j - c >= 0:
                        cover[i + j - c] += 1
                i = i + j + k + 1
    for i in range(n):
        if cover[i] == 0:
            return -1
    return cnt


print(min_machines(F, k))

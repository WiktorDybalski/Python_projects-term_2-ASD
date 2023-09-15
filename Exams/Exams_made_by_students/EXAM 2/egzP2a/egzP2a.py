from egzP2atesty import runtests


def partition(T, ind, p, r):
    x = T[ind[r]][1]
    i = p - 1
    for j in range(p, r):
        if T[ind[j]][1] >= x:
            i += 1
            T[ind[i]], T[ind[j]] = T[ind[j]], T[ind[i]]
    T[ind[i + 1]], T[ind[r]] = T[ind[r]], T[ind[i + 1]]
    return i + 1


def Quick_Select(T, ind, p, k, r):
    if p < r:
        q = partition(T, ind, p, r)
        if q < k:
            Quick_Select(T, ind, q + 1, k, r)
        elif q > k:
            Quick_Select(T, ind, p, k, q - 1)
    return


def zdjecie(T, m, k):
    n = len(T)
    start = [0 for _ in range(m)]
    end = [0 for _ in range(m)]

    akt_end = -1
    akt_width = k + m - 1
    for i in range(m):
        start[i] = akt_end + 1
        akt_end += akt_width
        end[i] = akt_end
        akt_width -= 1

    ind = [0 for _ in range(n)]
    items = 0
    col = 0
    row = 0
    while items < n:
        if start[row] + col <= end[row]:
            ind[start[row] + col] = items
            items += 1
        row += 1
        if row >= m:
            row = 0
            col += 1
    last_end = end[m - 1]
    for i in range(m - 2, -1, -1):
        Quick_Select(T, ind, 0, end[i], last_end)
        last_end = end[i] - 1
    return None


runtests(zdjecie, all_tests=True)

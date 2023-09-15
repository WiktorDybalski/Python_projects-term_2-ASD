# Longest increasing subsequence

def Binary_Search(tab, x):
    n = len(tab)
    L = 0
    R = n - 1
    if tab[L] == x:
        return L
    if tab[R] == x:
        return R

    while L <= R:
        mid = (L + R) // 2
        if tab[mid] == x:
            return mid
        if tab[mid] < x:
            L = mid
        else:
            R = mid


def lis(A):
    n = len(A)
    F = [1] * n
    parent = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                parent[i] = j
                F[i] = F[j] + 1
    big = max(A)
    index = Binary_Search(A, big)
    return big, A, parent, index


def func_lis(array):
    liss = []
    result = lis(array)

    def create_solution(A, parent, i):
        if parent[i] != -1:
            create_solution(A, parent, parent[i])
        liss.append(A[i])

    create_solution(result[1], result[2], result[3])
    return liss


def print_solution(A, parent, i):
    if parent[i] != -1:
        print_solution(A, parent, parent[i])
    print(A[i])


array = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]
result = lis(array)
print_solution(result[1], result[2], result[3])


def Binary_Search_rev(tab, x):
    n = len(tab)
    L = 0
    R = n - 1
    if tab[L] == x:
        return L
    if tab[R] == x:
        return R

    while L <= R:
        mid = (L + R) // 2
        if tab[mid] == x:
            return mid
        if tab[mid] > x:
            L = mid
        else:
            R = mid


def lds(A):
    n = len(A)
    F = [1] * n
    parent = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] > A[i] and F[j] + 1 > F[i]:
                parent[i] = j
                F[i] = F[j] + 1
    small = min(A)
    index = Binary_Search_rev(A, small)
    return small, A, parent, index


def func_lds(array):
    liss = []
    result = lds(array)

    def create_solution(A, parent, i):
        if parent[i] != -1:
            create_solution(A, parent, parent[i])
        liss.append(A[i])

    create_solution(result[1], result[2], result[3])
    return liss


result2 = func_lds(array)
result1 = func_lis(array)
print(result1)
print(result2)


def lis(T, dp, i):
    inf = float('inf')
    if i == 0:
        return 1
    if dp[i] != -inf:
        return dp[i]
    maxx = 1
    for j in range(i):
        if T[j] <= T[i]:
            maxx = max(maxx, lis(T, dp, j) + 1)
    dp[i] = maxx
    return dp[i]

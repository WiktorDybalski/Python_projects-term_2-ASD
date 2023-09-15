from ASD.Algorithms.Dynamic.Longest_increasing_subsequence import Binary_Search_rev
from zad1testy import runtests


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
    return parent


def func_lis(array):
    liss = []
    result = lis(array)
    return result


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
    return parent


def func_lds(array):
    result = lds(array)
    return result


def find_max(X):
    n = len(X)
    the_biggest = 0
    index = 0
    for i in range(n):
        if the_biggest < X[i]:
            the_biggest = X[i]
            index = i
    return the_biggest, index


def create_lis(array, parrent, index, moved):
    liss = []

    def create_solution(A, parent, i):
        if parent[i - moved] != -1:
            create_solution(A, parent, parent[i - moved])
        liss.append(A[i])

    create_solution(array, parrent, index)
    return liss


def mr(X):
    lis = func_lis(X)
    lds = func_lds(X)
    big1 = max(lis)
    big2 = max(lds)

    n = len(X)
    for index in range(1, n - 1):
        first = lds[0:index]
        second = lis[index: n]
        max1, index1 = find_max(first)
        max2, index2 = find_max(second)
        if max1 + max2 > big1 and max1 + max2 > big2:
            sol1 = create_lis(X, first, index1, index)
            sol2 = create_lis(X, second, index2, index)
            the_biggest = sol1 + sol2
    return the_biggest


runtests(mr)

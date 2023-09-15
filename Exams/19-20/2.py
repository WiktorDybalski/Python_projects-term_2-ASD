# 2pkt.] Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową

import random

T = [random.randint(150, 200) for _ in range(30)]


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def Quick_Select(T, a, b, k):
    if a == b:
        return T[a]
    n = len(T)
    while a < b:
        q = partition(T, a, b)
        if k == q:
            return
        elif k < q:
            b = q - 1
        else:
            a = q + 1


def section(T, p, q):
    print(T)
    Quick_Select(T, 0, len(T) - 1, p)
    print(T)
    Quick_Select(T, p + 1, len(T) - 1, q)
    print(T)
    return T[p:q + 1]


print(section(T, 5, 13))

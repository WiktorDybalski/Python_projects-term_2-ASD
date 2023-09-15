# Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
# są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak
# aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
# a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
# Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
# jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
# podać złożoność czasową i pamięciową zaproponowanego algorytmu.
# Przykład. Dla tablicy:
T = [[2, 3, 5],
     [7, 11, 13],
     [17, 19, 23]]


# wynikiem jest, między innymi tablica:
# T = [ [13,19,23],
#       [ 3, 7,17],
#       [ 5, 2,11] ]


def MergeSort(T):
    n = len(T)
    if n > 1:
        n //= 2
        L = T[:n]
        R = T[n:]

        MergeSort(L)
        MergeSort(R)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            T[k] = R[j]
            j += 1
            k += 1
        return T


# def find_median(T):
def print_array(A):
    for el in A:
        print(el)
    print("------------")


def Median(T):
    n = len(T)
    T_copy = []
    k = 0
    for i in range(n):
        for j in range(n):
            T_copy.append(T[i][j])
            k += 1
    T_copy = MergeSort(T_copy)

    for k in range(n):
        n_copy = len(T_copy)
        median = n_copy // 2
        T[k][k] = T_copy[median]
        T_copy.remove(T_copy[median])
    z = 0
    T_copy = T_copy[::-1]
    for l in range(n):
        for m in range(n):
            if l == m:
                continue
            T[l][m] = T_copy[z]
            z += 1
    return T


print_array(T)
Median(T)
print_array(T)

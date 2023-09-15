# [2pkt.] Zadanie 1. Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T)
# która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

from math import log10, floor

A = [123, 114577, 455, 1266, 2344, 67333]


def il_jedno_i_wielo(num):
    dl = floor(log10(num) + 1)
    counters = [0 for _ in range(10)]
    jedno = 0
    wielo = 0
    while num > 0:
        counters[num % 10] += 1
        num //= 10
    for el in counters:
        if el == 1:
            jedno += 1
        elif el > 1:
            wielo += 1
    return jedno, wielo


def Counting_Sort_for_index(arr, index):
    n = len(arr)
    max_val = arr[0][index]
    for i in range(1, n):
        if arr[i][index] > max_val:
            max_val = arr[i][index]
    count = [0] * (max_val + 1)
    for i in range(n):
        count[arr[i][index]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    result = [None] * n
    for i in range(n - 1, -1, -1):
        result[count[arr[i][index]] - 1] = arr[i]
        count[arr[i][index]] -= 1
    return result


def pretty_sort(A):
    n = len(A)
    tab = [[0 for _ in range(3)] for z in range(n)]
    for i in range(n):
        tab[i][0] = A[i]
        tab[i][1] = il_jedno_i_wielo(A[i])[0]
        tab[i][2] = il_jedno_i_wielo(A[i])[1]
    print(tab)
    tab = Counting_Sort_for_index(tab, 2)
    print(tab)
    tab = tab[::-1]
    print(tab)
    tab = Counting_Sort_for_index(tab, 1)
    tab = tab[::-1]
    return tab


print(pretty_sort(A))

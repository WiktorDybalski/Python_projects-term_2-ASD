# [2pkt.] Zadanie 3.
# Szablon rozwiązania: zad2.py
# Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a
# x
# , gdzie a to pewna stała większa od 1 (a > 1) zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
# Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i
# zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej. Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność
# obliczeniową. Nagłówek funkcji fast sort powinien mieć postać:
# def fast_sort(tab, a):
# ...
from math import log10

T = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


def give_x(a, y):
    return log10(y) / log10(a)


def Bubble_Sort(a):
    n = len(a)
    change = True
    x = -1
    while change:
        x += 1
        change = False
        for i in range(n - x - 1):
            if a[i][1] > a[i + 1][1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                change = True
    return a


def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Przypisz każdy element do odpowiedniego kubełka
    for value in arr:
        index = int(value[1] * n)
        buckets[index] = value

    # Sortowanie każdego kubełka
    for i in range(n):
        buckets[i] = Bubble_Sort(buckets[i])

    # Łączenie posortowanych kubełków
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


def fast_sort(tab, a):
    n = len(tab)
    tab_mod = [[0 for _ in range(2)] for z in range(n)]
    for i in range(n):
        tab_mod[i][0] = tab[i]
        tab_mod[i][1] = give_x(a, tab[i])
    print(tab_mod)
    bucket_sort(tab_mod)
    print(tab_mod)


fast_sort(T, 130)

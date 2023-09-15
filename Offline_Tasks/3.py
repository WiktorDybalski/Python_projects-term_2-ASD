# Mówimy, że dwa napisy są sobie równoważne, jeśli albo są identyczne, albo byłyby identyczne,
# gdyby jeden z nich zapisać od tyłu. Na przykład napisy “kot” oraz “tok” są sobie równoważne,
# podobnie jak napisy “pies” i “pies”. Dana jest tablica T zawierająca n napisów o łącznej długości
# N (każdy napis zawiera co najmniej jeden znak, więc N ≥ n; w praktyce można przyjąć, że N ≫ n;
# każdy napis składa się wyłącznie z małych liter alfabetu łacińskiego). Siłą napisu T[i] jest liczba
# indeksów j takich, że napisy T[i] oraz T[j] są sobie równoważne. Napis T[i] jest najsilniejszy, jeśli
# żaden inny napis nie ma większej siły.
# Proszę zaimplementować funkcję strong string(T), która zwraca siłę najsilniejszego napisu z
# tablicy T. Na przykład dla wejścia:
# # 0 1 2 3 4 5 6
# T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
# wywołanie strong string(T) powinno zwrócić 3. Algorytm powinien być możliwie jak najszybszy.
# Zadanie można rozwiązać w czasie O(N + nlog n), gdzie N to łączna długość napisów w tablicy
# wejściowej a n to liczba wyrazów.


def napis_na_liczbe(word):
    liczba = 0
    for i in range(len(word)):
        liczba += ord(word[i])
    return liczba


def if_the_same(word1, word2):
    return word1 == word2 or word1 == word2[::-1]


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parrent(i):
    return (i - 1) // 2


def build_heap(A):
    n = len(A)
    for i in range(parrent(n - 1), -1, - 1):
        heapify(A, i, n)


def heapify(A, i, n):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and len(A[l]) > len(A[max_ind]):
        max_ind = l
    if r < n and len(A[r]) > len(A[max_ind]):
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)


def Heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)
    return A


def strong_string(T):
    max_sila = 1
    n = len(T)
    T = Heap_sort(T)
    for i in range(n):
        cnt = 1
        # A = T[i+1:n-max_sila + 1]
        # print(A)
        for j in range(i + 1, n - max_sila):
            if len(T[i]) < len(T[j]):
                max_sila = max(max_sila, cnt)
                break
            if if_the_same(T[i], T[j]):
                cnt += 1
    return max_sila

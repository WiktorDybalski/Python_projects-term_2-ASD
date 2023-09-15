# Dana talica n (n >= 11) w zakresie [0, k]. Zamieniono 10 liczb z tej tablicy na losowe liczby spoza zakresu (np. dużo
# większe lub ujemne). Napisz algorytm, który posortuje tablicę w czasie O(n).
k = 20
T = [4, 2, 7, 1, 6, 17, 8, 13, 12, 14, 20, 18, 9, 10, 3]
T_mod = [78, 2, 45, 2256, -5, 23, 13, 12, 534, 121, -1, -8, 10, 3]


def Quick_Sort(T):
    n = len(T)
    if n <= 1:
        return T
    else:
        bigger = []
        smaller = []
        pivot = T[n - 1]
        for el in T[:n - 1]:
            if el <= pivot:
                smaller.append(el)
            else:
                bigger.append(el)
        return Quick_Sort(smaller) + [pivot] + Quick_Sort(bigger)


def Counting_Sort(array, k):
    n = len(array)
    amount_of_el = [0 for _ in range(k + 1)]
    sorted_array = [0 for z in range(n)]
    for i in range(n):
        amount_of_el[array[i]] += 1

    for j in range(1, k + 1):
        amount_of_el[j] += amount_of_el[j - 1]

    for s in range(n):
        sorted_array[amount_of_el[array[s]] - 1] = array[s]
        amount_of_el[array[s]] -= 1
    return sorted_array


def func(T, k):
    n = len(T)
    T1 = []
    T2 = []
    for i in range(n):
        if T[i] > k or T[i] < 0:
            T2.append(T[i])
        else:
            T1.append(T[i])
    T1 = Counting_Sort(T1, k)
    T2 = Quick_Sort(T2)
    sorted_tab = []
    m = 0
    n = 0
    while m < len(T1) and n < len(T2):
        if T1[m] >= T2[n]:
            sorted_tab.append(T2[n])
            n += 1
        else:
            sorted_tab.append(T1[m])
            m += 1
    while n < len(T2):
        sorted_tab.append(T2[n])
        n += 1
    return sorted_tab


print(func(T_mod, k))

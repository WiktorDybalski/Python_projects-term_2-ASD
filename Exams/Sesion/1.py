# Tablica k - chaotyczna. Zwrócić indeks nieuporządkowania k
T = [0, 2, 1, 2]


def Merge_Sort(T, index):
    n = len(T)
    if n > 1:
        mid = n // 2
        L = T[:mid]
        R = T[mid:]

        Merge_Sort(L, index)
        Merge_Sort(R, index)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][index] <= R[j][index]:
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


def chaos_index(T):
    n = len(T)
    cnt = 0
    max_cnt = 0
    T_mod = [[0 for _ in range(2)] for z in range(n)]
    for i in range(n):
        T_mod[i][0] = T[i]
        T_mod[i][1] = i
    print(T_mod)
    Merge_Sort(T_mod, 0)
    print(T_mod)
    for j in range(n):
        cnt = abs(T_mod[j][1] - j)
        max_cnt = max(max_cnt, cnt)
    return max_cnt


print(chaos_index(T))

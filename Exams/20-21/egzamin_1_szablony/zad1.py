from zad1testy import runtests


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
            if L[i][0] <= R[j][0]:
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


def chaos_index(T):
    n = len(T)
    if n == 1 or n == 0:
        return 0
    new_T = [0 for _ in range(n)]
    the_biggest = 0
    for i in range(n):
        T[i] = (T[i], i)
    new_T = [T[i] for i in range(n)]
    new_new_T = MergeSort(new_T)
    for i in range(0, n):
        the_biggest = max(the_biggest, abs(new_new_T[i][1] - i))
    return the_biggest


runtests(chaos_index)

from egzP6atesty import runtests


def MergeSort(T, H, index):
    n = len(T)
    if n > 1:
        n //= 2
        L = T[:n]
        R = T[n:]
        LH = H[:n]
        RH = H[n:]

        MergeSort(L, LH, index)
        MergeSort(R, RH, index)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i][index] <= R[j][index]:
                T[k] = L[i]
                H[k] = LH[i]
                i += 1
            else:
                T[k] = R[j]
                H[k] = RH[j]
                j += 1
            k += 1

        while i < len(L):
            T[k] = L[i]
            H[k] = LH[i]
            i += 1
            k += 1

        while j < len(R):
            T[k] = R[j]
            H[k] = RH[j]
            j += 1
            k += 1
        return H


def google(H, s):
    n = len(H)
    memo = [0 for _ in range(n)]
    for i in range(n):
        amount_of_letters = 0
        n_word = len(H[i])
        for letter in H[i]:
            if not letter.isdigit():
                amount_of_letters += 1
        memo[i] = [n_word, amount_of_letters]
    H = MergeSort(memo, H, 1)
    H = MergeSort(memo, H, 0)
    H = H[::-1]
    return H[s - 1]


runtests(google, all_tests=True)

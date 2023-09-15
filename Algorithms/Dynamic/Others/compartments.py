# Algortyhm return the maximal amount of separable compartments

T = [(1, 7), (6, 9), (3, 5), (2, 3), (5, 7), (8, 9), (3, 4)]


def separable(T):
    n = len(T)
    T = sorted(T, key=lambda x: x[1])
    storage = []
    i = 0
    storage.append(T[i])
    while i < n - 1:
        com = T[i]
        for j in range(i + 1, n):
            if com[1] < T[j][0]:
                storage.append(T[j])
                i = j
                break
    return storage, len(storage)


print(separable(T))

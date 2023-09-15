from egz2atesty import runtests


def coal(A, T):
    n = len(A)
    nn = n
    full = [False for _ in range(nn)]
    capacity = [0 for _ in range(nn)]
    j = 0
    last = 0
    for i in range(n):
        coal = A[i]
        j = 0
        while True:
            if not full[j] and capacity[j] + coal <= T:
                capacity[j] += coal
                last = j
                if capacity[j] == T:
                    full[j] = True
                    j += 1
                break
            else:
                j += 1
    return last


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(coal, all_tests=True)

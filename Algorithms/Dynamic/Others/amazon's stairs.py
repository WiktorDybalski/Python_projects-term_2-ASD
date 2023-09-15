# The algorithm returns the number of possibilities to get from field 0 to field n - 1

T = [1, 3, 2, 1, 0]


def amount_of_possibilities(T):
    n = len(T)
    possibilities = [0 for _ in range(n)]
    possibilities[0] = 1
    for i in range(0, n):
        rangee = T[i]
        for j in range(1, rangee + 1):
            if i + j <= n - 1:
                possibilities[i + j] += 1
    return possibilities[n - 1]


print(amount_of_possibilities(T))

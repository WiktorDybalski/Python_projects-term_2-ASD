from egz1btesty import runtests


def planets(D, C, T, E):
    n = len(D)
    f = [[float('inf') for _ in range(E + 1)] for _ in range(n)]
    for i in range(E + 1):
        f[0][i] = C[0] * i

    planet = T[0][0]
    cost = T[0][1]
    f[planet][0] = cost + f[0][0]
    for i in range(1, n):
        for b in range(E + 1):
            dist = D[i] - D[i - 1]
            if b + dist < E:
                first = f[i - 1][b + dist]
            else:
                first = f[i - 1][E] + C[i] * (b + dist - E)
            if b > 0:
                second = f[i][b - 1] + C[i]
            else:
                second = float('inf')
            f[i][b] = min(first, second, f[i][b])
            if b == 0:
                planet = T[i][0]
                cost = T[i][1]
                f[planet][0] = min(f[planet][0], f[i][b] + cost)
    return min(f[n - 1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)

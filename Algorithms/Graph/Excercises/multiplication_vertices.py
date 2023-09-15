G = [[(1, 1)],
     [(0, 1), (2, 1)],
     [(1, 2), (3, 1), (4, 2)],
     [(2, 1), (4, 2), (5, 6)],
     [(2, 3), (3, 2), (5, 4)],
     [(3, 6), (4, 4), (6, 2)],
     [5, 2]]

prize = [3, 4, 2, 1, 5, 7, 2]


def multiplication_vertices(G, start, end, value, prize):
    n = len(G)
    new_G = [[] for _ in range(n * value)]
    new_n = len(new_G)
    for v in range(n):
        for i in range(value - 1):
            new_G[v * value + i] += [(v * value + i + 1, prize[v])]

    for i in range(0, n):
        for j in range(0, value):
            for k in range(len(G[i])):
                if j >= G[i][k][1]:
                    new_G[value * k + j] += [(G[i][k][0] * value + j - 1, 0)]
                    new_G[G[i][k][0] * value + j - 1] += [(value * k + j, 0)]


multiplication_vertices(G, 0, 6, 2, prize)

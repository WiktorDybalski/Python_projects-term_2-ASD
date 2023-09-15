G = [(0, 1), (0, 3), (2, 3), (3, 1)]


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        p = q + 1


def edges_to_adjacency(edges):
    n = len(edges)
    the_biggest = 0
    for i in range(n):
        temp = max(edges[i][0], edges[i][1])
        if temp > the_biggest:
            the_biggest = temp

    array = [[] for _ in range(the_biggest + 1)]
    for j in range(n):
        first = edges[j][0]
        second = edges[j][1]
        array[first].append(second)
        array[second].append(first)
    for k in range(the_biggest + 1):
        quick_sort(array[k], 0, len(array[k]) - 1)
    return array


def BFS(G, s):
    n = len(G)
    visited = [False] * n
    d = [-1] * n
    parrent = [None] * n
    queue = []

    queue.append(s)
    visited[s] = True
    d[s] = 0
    parrent[0] = [None]

    while queue:
        u = queue.pop(0)

        for v in G[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                d[v] = d[u] + 1
                parrent[v] = u
    return d


def func(G):
    n = len(G)
    G = edges_to_adjacency(G)
    days = BFS(G, 0)
    days1 = [0 for _ in range(max(days) + 1)]
    for i in range(n):
        days1[days[i]] += 1
    the_best = 0
    index = 0
    for j in range(max(days) + 1):
        if days1[j] > the_best:
            the_best = days1[j]
            index = j
    return index


print(func(G))

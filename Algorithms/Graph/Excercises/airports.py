# Algorythm for finding the minimal cost of build a road between two cities or a airport between two cities.
import heapq

G = [(0, 1, 7), (1, 2, 8), (1, 3, 10), (2, 4, 6), (4, 5, 7)]
K = 9


def find_max(G):
    n = len(G)
    big = 0
    for i in range(n):
        big = max(big, G[i][0])
        big = max(big, G[i][1])
    return big


def find(v, parent, rank):
    while parent[v] != v:
        v = parent[v]
    return v


def union(u, v, parent, rank):
    x = find(u, parent, rank)
    y = find(v, parent, rank)
    if rank[x] > rank[y]:
        parent[y] = x
        return x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1
        return y


def partition(A, p, r, index):
    x = A[r][index]
    i = p - 1
    for j in range(p, r):
        if A[j][index] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort_for_i_index(A, p, r, i):
    while p < r:
        q = partition(A, p, r, i)
        quick_sort_for_i_index(A, p, q - 1, i)
        p = q + 1
    return A


def Kruskal_MST_min(G):
    n = find_max(G) + 1
    parents = [i for i in range(n)]
    rank = [0 for i in range(n)]
    G = quick_sort_for_i_index(G, 0, n - 2, 2)
    mst = []
    for i in range(n - 1):
        u = G[i][0]
        v = G[i][1]
        x = find(u, parents, rank)
        y = find(v, parents, rank)
        if x != y:
            mst.append((u, v, G[i][2]))
            union(x, y, parents, rank)
    return mst


def airports(G):
    G = Kruskal_MST_min(G)
    return G


print(airports(G))

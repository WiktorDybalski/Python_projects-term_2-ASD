# Algorithm: Kruskala's Algorythm for finding the minimal/maximal spanning tree for acyclic, indirected, weighted graphs
# Complexity: O(E * logV)

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
    n = len(G)
    parents = [i for i in range(n)]
    rank = [0 for i in range(n)]
    G = quick_sort_for_i_index(G, 0, n - 1, 2)
    mst = []
    for i in range(n):
        u = G[i][0]
        v = G[i][1]
        x = find(u, parents, rank)
        y = find(v, parents, rank)
        if x != y:
            mst.append((u, v, G[i][2]))
            union(x, y, parents, rank)
    return mst


def Kruskal_MST_max(G):
    n = len(G)
    parents = [i for i in range(n)]
    rank = [0 for i in range(n)]
    G = quick_sort_for_i_index(G, 0, n - 1, 2)
    G = G[::-1]
    mst = []
    for i in range(n):
        u = G[i][0]
        v = G[i][1]
        x = find(u, parents, rank)
        y = find(v, parents, rank)
        if x != y:
            mst.append((u, v, G[i][2]))
            union(x, y, parents, rank)
    return mst


G = [(0, 1, 1), (1, 2, 3), (2, 3, 6), (3, 4, 2), (4, 5, 7), (0, 5, 8), (0, 4, 5), (2, 4, 4)]
print(Kruskal_MST_min(G))
print(Kruskal_MST_max(G))

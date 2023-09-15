# Depth-First Search Algorythm
# O(V + E) for adjacency list
G = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12],
     [10, 11]]


def DFS(G):
    def DFS_Visit(G, u):
        nonlocal time
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_Visit(G, v)
        time += 1

    n = len(G)
    visited = [False] * n
    parent = [None] * n
    time = 0
    for v in range(n):
        if not visited[v]:
            DFS_Visit(G, v)
    return parent


print(DFS(G, 0, 12))

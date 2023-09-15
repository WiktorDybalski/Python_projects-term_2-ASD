from collections import deque


# O(V + E) for adjacency list

# Zastosowanie:  Wyznaczenie kolejności wykonywania zadania jeśli jedno zadanie musi być wykonane przed drugim


def topological_sort(G):
    sorted_array = []

    def DFS_Visit(G, u):
        nonlocal time, sorted_array
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_Visit(G, v)
        sorted_array.append(u)
        time += 1

    n = len(G)
    visited = [False] * n
    parent = [None] * n
    time = 0
    for v in range(n):
        if not visited[v]:
            DFS_Visit(G, v)
    return sorted_array[::-1]


G = [[1, 2], [2, 4], [], [], [3, 6], [4], []]
print(topological_sort(G))

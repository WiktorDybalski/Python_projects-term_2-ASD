# Algoryth finds bridges in graph
# Complexity: O(V + E)

def DFS(G):
    def DFS_Visit(G, u):
        nonlocal time, times, low
        time += 1
        times[u] = time
        low[u] = time
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
    times = [0 for _ in range(n)]
    low = [0 for _ in range(n)]
    for v in range(n):
        if not visited[v]:
            DFS_Visit(G, v)
    return times, low


def DFS_modd(G, times, low):
    def DFS_Visit(G, u):
        nonlocal time, times, low
        time += 1
        visited[u] = True
        for v in G[u]:
            if visited[v]:
                if parent[u] != v:
                    low[u] = min(low[u], low[v])
            else:
                parent[v] = u
                DFS_Visit(G, v)
                low[u] = min(low[u], low[v])
        time += 1

    n = len(G)
    visited = [False] * n
    parent = [None] * n
    time = 0
    for v in range(n):
        if not visited[v]:
            DFS_Visit(G, v)
    bridges = []
    for i in range(n):
        if times[i] == low[i] and parent[i] is not None:
            bridges.append([parent[i], i])
    return times, low, bridges


def find_bridges(G):
    n = len(G)
    times, low = DFS(G)
    times, low, bridges = DFS_modd(G, times, low)

    print("times:", times)
    print("low:", low)
    print("bridges:", bridges)
    return times, low, bridges


G = [[1, 6],
     [0, 2],
     [1, 3, 6],
     [2, 4, 5],
     [3, 5],
     [3, 4],
     [0, 2, 7],
     [6]]

find_bridges(G)

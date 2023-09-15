from egzP5btesty import runtests


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
            bridges.append(parent[i])
    return times, low, bridges


def find_bridges(G):
    n = len(G)
    times, low = DFS(G)
    times, low, bridges = DFS_modd(G, times, low)
    return bridges


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
        array[k] = sorted(array[k])
    return array


def create(B):
    n = len(B)
    G = []
    for i in range(n):
        B[i] = sorted(B[i])
    B = sorted(B, key=lambda x: x[1])
    B = sorted(B, key=lambda x: x[0])
    i = 0
    while i < n:
        first = B[i][0]
        second = B[i][1]
        G.append([first, second])
        last = [first, second]
        for j in range(i + 1, n + 1):
            if j == n or last != B[j]:
                i = j - 1
                break
        i += 1

    G = edges_to_adjacency(G)
    return G


def koleje(B):
    G = create(B)
    points = find_bridges(G)
    right_points = set()
    for i in range(len(points)):
        right_points.add(points[i])
    result = len(right_points)
    return result


runtests(koleje, all_tests=True)

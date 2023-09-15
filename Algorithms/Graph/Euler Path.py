def has_euler_cycle_bfs(G):
    n = len(G)
    degree = [0] * n
    for u in range(n):
        degree[u] = len(G[u])

    if not all(d % 2 == 0 for d in degree):
        return False  # graf ma nieparzysty stopień, więc nie ma cyklu Eulera

    s = 0  # dowolny wierzchołek startowy
    visited = [False] * n
    visited[s] = True
    queue = [s]

    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    if not all(visited):
        return False  # graf nie jest spójny, więc nie ma cyklu Eulera

    # graf jest spójny i ma parzyste stopnie wierzchołków, więc wykonujemy BFS z dowolnego wierzchołka
    d = [-1] * n
    parent = [None] * n
    queue = [s]

    d[s] = 0
    parent[s] = None

    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                parent[v] = u
                queue.append(v)

    # jeśli BFS przeszukał cały graf, to graf ma cykl Eulera
    return all(d[u] >= 0 for u in range(n))

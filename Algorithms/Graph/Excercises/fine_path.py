import heapq


def relax(G, u, v, d, e, parent, visited, w):
    if d[v] > d[u] + w and e[v] > e[u] + 1:
        d[v] = d[u] + w
        parent[v] = u
        e[v] = e[u] + 1


def dijkstry(G, s):
    n = len(G)
    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    d[s] = 0
    visited = [False for _ in range(n)]
    e = [float('inf') for _ in range(n)]
    e[0] = 0
    pq = [(0, s)]
    while pq:
        curr_d, u = heapq.heappop(pq)
        for w, v in G[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))
            relax(G, u, v, d, e, parent, visited, w)
        visited[u] = True
    return d, parent


G = [[(7, 1)],
     [(7, 0), (8, 2), (10, 3), (14, 4)],
     [(8, 1), (6, 4)],
     [(10, 1)],
     [(6, 2), (14, 1), (7, 5)],
     [(7, 4)]]

print(dijkstry(G, 0))

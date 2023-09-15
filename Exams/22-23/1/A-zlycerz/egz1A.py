from egz1Atesty import runtests

import heapq


def change_v_and_w(Graph):
    n = len(Graph)
    new = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(Graph[i])):
            v = Graph[i][j][0]
            w = Graph[i][j][1]
            new[i].append([w, v])
    return new


def relax(G, u, v, d, parent, visited, w):
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        parent[v] = u


def dijkstry(G, s):
    n = len(G)
    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    d[s] = 0
    visited = [False for _ in range(n)]
    pq = [(0, s)]
    while pq:
        curr_d, u = heapq.heappop(pq)
        for w, v in G[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))
            relax(G, u, v, d, parent, visited, w)
        visited[u] = True
    return d


def change_graph(G, r):
    n = len(G)
    for i in range(n):
        for v in G[i]:
            v[0] = v[0] * 2 + r
    return G


def gold(G, V, s, t, r):
    n = len(G)
    G = change_v_and_w(G)
    d1 = dijkstry(G, s)
    G = change_graph(G, r)
    d2 = dijkstry(G, t)
    d = [0 for _ in range(n)]
    for i in range(n):
        d[i] = d1[i] + d2[i] - V[i]
    return min(d)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)

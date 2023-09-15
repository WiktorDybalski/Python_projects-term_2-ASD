# Dijkstry algorythm for Graphs
# The shortest path in Graph with wages >= 0
# Complexity: O(E*logV)
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


G = [[[1, 1], [2, 2]],  # 0
     [[0, 1], [3, 3], [4, 3]],  # 1
     [[0, 2], [3, 1], [5, 7]],  # 2
     [[1, 3], [2, 1], [6, 3], [7, 2]],  # 3
     [[1, 3], [7, 5]],  # 4
     [[2, 7], [6, 1], [8, 4]],  # 5
     [[3, 3], [5, 1], [8, 8]],  # 6
     [[3, 2], [4, 5], [8, 1]],  # 7
     [[5, 4], [6, 8], [7, 1]]]  # 8

G = change_v_and_w(G)
print(dijkstry(G, 0))

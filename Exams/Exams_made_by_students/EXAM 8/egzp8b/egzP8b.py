import heapq
from queue import PriorityQueue

from egzP8btesty import runtests


def adjacency_to_matrix(G):
    n = len(G)
    inf = float('inf')
    new_G = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        new_G[i][i] = 0
    for i in range(n):
        for edge in G[i]:
            wage = edge[1]
            first = i
            second = edge[0]
            new_G[first][second] = wage
            new_G[second][first] = wage
    return new_G


def Floyd_Warshall(G):
    n = len(G)
    inf = float('inf')
    distance = [[inf for i in range(n)] for j in range(n)]
    parent = [[None for i in range(n)] for j in range(n)]

    for p in range(n):
        for u in range(n):
            if G[p][u] == 0:
                distance[p][u] = inf
            else:
                distance[p][u] = G[p][u]
        distance[p][p] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                    parent[i][j] = parent[k][j]

    for i in range(n):

        if distance[i][i] < 0:
            return False
    return distance


def robot(G, P):
    G = adjacency_to_matrix(G)
    distance = Floyd_Warshall(G)
    n = len(P)
    output = 0
    for i in range(1, n):
        output += distance[P[i]][P[i - 1]]
    return output


# Complexity n^3 logn
# def change_v_and_w(Graph):
#     n = len(Graph)
#     new = [[] for _ in range(n)]
#     for i in range(n):
#         for j in range(len(Graph[i])):
#             v = Graph[i][j][0]
#             w = Graph[i][j][1]
#             new[i].append([w, v])
#     return new
#
#
# def relax(G, u, v, d, parent, visited, w):
#     if d[v] > d[u] + w:
#         d[v] = d[u] + w
#         parent[v] = u
#
#
# def dijkstry(G, s, t):
#     n = len(G)
#     d = [float('inf') for _ in range(n)]
#     parent = [None for _ in range(n)]
#     d[s] = 0
#     visited = [False for _ in range(n)]
#     pq = [(0, s)]
#     while pq:
#         curr_d, u = heapq.heappop(pq)
#         for w, v in G[u]:
#             if not visited[v]:
#                 heapq.heappush(pq, (w, v))
#             relax(G, u, v, d, parent, visited, w)
#         visited[u] = True
#     return d[t]
#
#
# def robot(G, P):
#     n = len(G)
#     d = 0
#     G = change_v_and_w(G)
#     for i in range(1, len(P)):
#         d += dijkstry(G, P[i - 1], P[i])
#     return d


runtests(robot, all_tests=True)

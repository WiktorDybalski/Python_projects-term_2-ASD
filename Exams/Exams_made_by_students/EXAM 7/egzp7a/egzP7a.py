from collections import deque

from egzP7atesty import runtests


def Ford_Fulkerson(g, source, sink):
    graph = g
    Max_Flow = 0
    parent = [-1] * len(graph)
    while BFS(graph, source, sink, parent):
        v = sink
        path_flow = float('inf')
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = parent[v]
        Max_Flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return Max_Flow


def BFS(graph, source, sink, parent):
    visited = [False for i in range(len(graph))]
    queue = deque()
    queue.append(source)
    visited[source] = True
    while len(queue) > 0:
        curr = queue.popleft()
        for neighbour in range(len(graph)):
            if visited[neighbour] == False and graph[curr][neighbour] > 0:
                visited[neighbour] = True
                parent[neighbour] = curr
                queue.append(neighbour)

    return visited[sink]



# Complexity: O(n^3)
def create(G, T):
    n = len(T)
    for i in range(1, n + 1):
        G[0][i] = 1
    for i in range(n + 1, 2 * n + 1):
        G[i][2 * n + 1] = 1
    for i in range(1, n + 1):
        pref = T[i - 1]
        for k in range(3):
            if pref[k] is not None:
                G[i][n + 1 + pref[k]] = 1
    return G


def akademik(T):
    n = len(T)
    without = 0
    for i in range(n):
        if T[i][0] is None and T[i][1] is None and T[i][2] is None:
            without += 1
    G = [[0 for _ in range(2 * n + 2)] for _ in range(2 * n + 2)]
    G = create(G, T)
    new_n = len(G)
    result = Ford_Fulkerson(G, 0, new_n - 1)
    output = n - result - without
    return output


runtests(akademik)

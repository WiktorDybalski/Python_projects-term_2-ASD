# Algoryth check if the graph is bipartite

def BFS_modd(G, s, t):
    n = len(G)
    visited = [False] * n
    d = [-1] * n
    parrent = [None] * n
    queue = []

    queue.append(s)
    visited[s] = True
    d[s] = 0
    parrent[0] = [None]

    while queue:
        u = queue.pop(0)
        print(u, end=" ")
        print(" ")
        print(d, end=" ")
        print(" ")

        for v in G[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                d[v] = d[u] + 1
                parrent[v] = u
    return d[t]


def is_bigraph(Graph):
    n = len(Graph)
    visited = [False] * n
    color = [None] * n
    queue = []

    queue.append(0)
    visited[0] = True
    color[0] = 1

    while queue:
        u = queue.pop(0)
        for v in Graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                color[v] = 1 - color[u]
            elif color[v] == color[u]:
                return False
    return True


print(is_bigraph([[1, 2], [0, 2], [0, 1, 3], [2]]))

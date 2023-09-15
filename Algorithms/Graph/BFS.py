# Basic Breadth-First Search algorythm
# Complexity: O(V + E)
# Graph Connectivity: To check graph connectivity, go through the visited array and check if every part of array is true
# The Shortest Path: To check or count the shortest path, we have to return the reversed Parents array
def BFS(G, s):
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

        for v in G[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                d[v] = d[u] + 1
                parrent[v] = u
    return d


G = [[1, 2], [0, 2], [0, 1, 3], [2]]

print(BFS(G, 0))


# from s to t algorythm

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

        for v in G[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                d[v] = d[u] + 1
                parrent[v] = u
    return d[t]


G = [[1, 2], [0, 2], [0, 1, 3], [2]]

print(BFS_modd(G, 0, 3))

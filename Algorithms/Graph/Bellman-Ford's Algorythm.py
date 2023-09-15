# Bellman-Ford's Algorythm
# The shortest path in graf with wages when wages can be negative
# Our Graph must be directed!!!
# Complexity: O(V * E)


def edges_to_adjacency_wages_directed(edges):
    n = len(edges)
    the_biggest = 0
    for i in range(n):
        temp = max(edges[i][0], edges[i][1])
        if temp > the_biggest:
            the_biggest = temp

    G = [[] for _ in range(the_biggest + 1)]
    for u, v, w in edges:
        G[u].append([v, w])
    return G


def relax(u, v, d, parent, w):
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        parent[v] = u


def bellman_ford(G, s):
    n = len(G)
    cycle = False
    parent = [None for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    d[s] = 0
    for i in range(n - 1):
        for u in range(n):
            for v, w in G[u]:
                relax(u, v, d, parent, w)
    # check if there is a negative cycle
    for u in range(n):
        for v, w in G[u]:
            if d[v] > d[u] + w:
                cycle = True
    if cycle:
        return None
    return d


G = [[0, 1, 2], [0, 2, 4], [1, 2, -1], [1, 3, 2], [2, 3, 3], [2, 4, 2], [3, 4, -4]]
s = 0
G = edges_to_adjacency_wages_directed(G)
distances = bellman_ford(G, s)
print(distances)

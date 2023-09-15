# Minimal and maximal spanning trees for acyclic, indirected, weighted graphs
# Complexity: O(E * logV)

import heapq
from queue import PriorityQueue


def edges_to_adjacency_wages(edges):
    n = len(edges)
    the_biggest = 0
    for i in range(n):
        temp = max(edges[i][0], edges[i][1])
        if temp > the_biggest:
            the_biggest = temp

    array = [[] for _ in range(the_biggest + 1)]
    for j in range(n):
        first = [edges[j][2], edges[j][0]]
        second = [edges[j][2], edges[j][1]]
        array[edges[j][0]].append(second)
        array[edges[j][1]].append(first)
    return array


def relax_to_min(u, curr_w, v, w, parent, visited, wages, pq):
    if w < wages[v] and not visited[v]:
        wages[v] = w
        parent[v] = u
        heapq.heappush(pq, (curr_w + w, v))


def Prime_minimal_spaning_trees(G, s):
    G = edges_to_adjacency_wages(G)
    mst = []
    n = len(G)
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    wages = [float("inf") for _ in range(n)]
    wages[s] = 0
    pq = []
    heapq.heappush(pq, (wages[s], s))
    while pq:
        curr_w, u = heapq.heappop(pq)
        visited[u] = True
        for w, v in G[u]:
            relax_to_min(u, curr_w, v, w, parent, visited, wages, pq)
    for i in range(n):
        if parent[i] is not None:
            mst.append((parent[i], i, wages[i]))
    return parent, wages, mst


G1 = [(0, 1, 1), (1, 2, 3), (2, 3, 6), (3, 4, 2), (4, 5, 7), (0, 5, 8), (0, 4, 5), (2, 4, 4)]

print(Prime_minimal_spaning_trees(G1, 2))


def relax_to_max(u, curr_w, v, w, parent, visited, wages, pq):
    if w > wages[v] and not visited[v]:
        wages[v] = w
        parent[v] = u
        heapq.heappush(pq, (-(curr_w + w), v))


def Prime_maximal_spaning_trees(G, s):
    G = edges_to_adjacency_wages(G)
    mst = []
    n = len(G)
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    wages = [float("-inf") for _ in range(n)]
    wages[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))
    while pq:
        curr_w, u = heapq.heappop(pq)
        curr_w = -curr_w
        visited[u] = True
        for w, v in G[u]:
            relax_to_max(u, curr_w, v, w, parent, visited, wages, pq)
    for i in range(n):
        if parent[i] is not None:
            mst.append((parent[i], i, wages[i]))
    return parent, wages, mst


G2 = [(0, 1, 1), (1, 2, 3), (2, 3, 6), (3, 4, 2), (4, 5, 7), (0, 5, 8), (0, 4, 5), (2, 4, 4)]
print(Prime_maximal_spaning_trees(G2, 2))


# Correct MIN MST
def MinimalST(G, start):
    # Algorytm Prima
    # G - adj list
    n = len(G)

    Q = PriorityQueue()
    parent = [None for _ in range(n)]
    D = [float('inf') for _ in range(n)]
    D[start] = 0
    visited = [False for _ in range(n)]
    suma = 0

    Q.put((0, start))

    while not Q.empty():

        d, curr_node = Q.get()
        visited[curr_node] = True

        for neighbour, distance in G[curr_node]:

            if not visited[neighbour]:

                if distance > D[neighbour]:
                    D[neighbour] = distance
                    parent[neighbour] = curr_node
                    Q.put((distance, neighbour))

    for i in range(n):
        suma += D[i]

    print(suma)


# Correct MAX MST
def MaximalST(G, start):
    # Algorytm Prima
    # G - adj list
    n = len(G)

    Q = PriorityQueue()
    parent = [None for _ in range(n)]
    D = [float('-inf') for _ in range(n)]
    D[start] = 0
    visited = [False for _ in range(n)]
    suma = 0

    Q.put((0, start))

    while not Q.empty():

        d, curr_node = Q.get()
        visited[curr_node] = True

        for neighbour, distance in G[curr_node]:

            if not visited[neighbour]:

                if distance > D[neighbour]:
                    D[neighbour] = distance
                    parent[neighbour] = curr_node
                    Q.put((-distance, neighbour))

    for i in range(n):
        suma += D[i]

    print(suma)

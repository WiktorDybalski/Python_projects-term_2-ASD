import heapq


def edges_to_adjacency_wages(edges):
    n = len(edges)
    the_biggest = 0
    for i in range(n):
        temp = max(edges[i][0], edges[i][1])
        if temp > the_biggest:
            the_biggest = temp

    array = [[] for _ in range(the_biggest + 1)]
    for j in range(n):
        first = [edges[j][0], edges[j][2]]
        second = [edges[j][1], edges[j][2]]
        array[edges[j][0]].append(second)
        array[edges[j][1]].append(first)
    return array


def dijkstra(n, G, a, b):
    distances = [float('inf') for _ in range(n)]
    parent = [None for o in range(n)]
    distances[a] = 0
    parent[a] = None
    visited = [False for p in range(n)]
    counter = [0 for z in range(n)]
    pq = [(0, a)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        for neighbor, weight in G[current_vertex]:
            if visited[neighbor]:
                continue
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_vertex
                counter[neighbor] = counter[parent[neighbor]] + 1
                visited[current_vertex] = True
                heapq.heappush(pq, (distance, neighbor))
        if current_vertex == b and distances[b] != float('inf'):
            if counter[L] >= 4:
                return distances[b]

    return None


def turysta(G, D, L):
    G = edges_to_adjacency_wages(G)
    n = len(G)
    the_shortest_path = dijkstra(n, G, D, L)
    return the_shortest_path


G = [
    (0, 1, 9), (0, 2, 1),
    (1, 2, 2), (1, 3, 8),
    (1, 4, 3), (2, 4, 7),
    (2, 5, 1), (3, 4, 7),
    (4, 5, 6), (3, 6, 8),
    (4, 6, 1), (5, 6, 1)
]
D = 0
L = 6

print(turysta(G, D, L))
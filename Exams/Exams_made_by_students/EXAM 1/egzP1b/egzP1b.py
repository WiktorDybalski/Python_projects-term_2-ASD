from egzP1btesty import runtests

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
        first = [edges[j][0], edges[j][2]]
        second = [edges[j][1], edges[j][2]]
        array[edges[j][0]].append(second)
        array[edges[j][1]].append(first)
    return array


def turysta(G, D, L):
    G = edges_to_adjacency_wages(G)
    n = len(G)

    start = D
    end = L

    n = len(G)
    visited = [[False for _ in range(5)] for _ in range(n)]
    D = [[float('inf') for _ in range(5)] for _ in range(n)]

    for i in range(5):
        D[start][i] = 0

    Q = PriorityQueue()
    Q.put((0, (start, 0)))

    while not Q.empty():

        curr_dist, node = Q.get()

        curr_node = node[0]
        odw = node[1]

        if curr_node == end and odw == 4:
            return curr_dist

        if not visited[curr_node][odw] and odw < 4:

            visited[curr_node][odw] = True

            for neighbour, d in G[curr_node]:

                if not visited[neighbour][odw + 1]:

                    new_dist = curr_dist + d

                    if new_dist < D[neighbour][odw + 1]:
                        D[neighbour][odw + 1] = new_dist
                        Q.put((new_dist, (neighbour, odw + 1)))
    return D[end][4]


runtests(turysta)

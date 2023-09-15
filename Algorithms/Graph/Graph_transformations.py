# From Array_of_edges to Adjacency array

Array_of_edges = [[0, 1], [1, 6], [6, 4], [4, 7], [4, 2], [2, 3], [3, 0], [0, 5]]


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        p = q + 1


def edges_to_adjacency(edges):
    n = len(edges)
    the_biggest = 0
    for i in range(n):
        temp = max(edges[i][0], edges[i][1])
        if temp > the_biggest:
            the_biggest = temp

    array = [[] for _ in range(the_biggest + 1)]
    for j in range(n):
        first = edges[j][0]
        second = edges[j][1]
        array[first].append(second)
        array[second].append(first)
    for k in range(the_biggest + 1):
        quick_sort(array[k], 0, len(array[k]) - 1)
    return array


print(edges_to_adjacency(Array_of_edges))

# From Array_of_edges to Adjacency array (with Wages)

edges = [(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]


def change_v_and_w(Graph):
    n = len(Graph)
    new = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(Graph[i])):
            v = Graph[i][j][0]
            w = Graph[i][j][1]
            new[i].append([w, v])
    return new


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


def edges_to_adjacency_wages_directed(edges):
    n = len(edges)
    G = [[] for _ in range(n)]
    for u, v, w in range(n):
        G[u].append([v, w])
    return G


print(edges_to_adjacency_wages(edges))

matrix = [[None, 1, 0, 1, 0, 1, 0, 0],  # 0
          [1, None, 0, 0, 1, 0, 1, 0],  # 1
          [0, 0, None, 1, 1, 0, 0, 0],  # 2
          [1, 0, 1, None, 0, 0, 0, 0],  # 3
          [0, 1, 1, 0, None, 0, 0, 1],  # 4
          [1, 0, 0, 0, 0, None, 0, 0],  # 5
          [0, 1, 0, 0, 0, 0, None, 0],  # 6
          [0, 0, 0, 0, 1, 0, 0, None]]  # 7


def add_v(E, first, second):
    n = len(E)
    E[first].append(second)
    E[second].append(first)
    return E


def matrix_to_adjacency(matrix):
    n = len(matrix)
    array = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j]:
                array = add_v(array, i, j)
    return array


print(matrix_to_adjacency(matrix))

matrix_of_wages = [[None, 2, 0, 7, 0, 1, 0, 0],  # 0
                   [2, None, 0, 0, 5, 0, 3, 0],  # 1
                   [0, 0, None, 8, 1, 0, 0, 0],  # 2
                   [7, 0, 8, None, 0, 0, 0, 0],  # 3
                   [0, 5, 1, 0, None, 0, 0, 11],  # 4
                   [1, 0, 0, 0, 0, None, 0, 0],  # 5
                   [0, 3, 0, 0, 0, 0, None, 0],  # 6
                   [0, 0, 0, 0, 11, 0, 0, None]]  # 7


def add_v_wages(E, first, second, wage):
    E[first].append([second, wage])
    E[second].append([first, wage])
    return E


def matrix_to_adjacency_wages(matrix):
    n = len(matrix)
    array = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j]:
                array = add_v_wages(array, i, j, matrix[i][j])
    return array


print(matrix_to_adjacency_wages(matrix_of_wages))


def adjacency_to_edges(array):
    n = len(array)
    edges = []
    for i in range(n):
        for w, v in array[i]:
            if v > i:
                edges.append((i, v, w))
    return edges

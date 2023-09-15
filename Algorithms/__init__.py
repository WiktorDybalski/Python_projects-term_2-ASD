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
    print(parent)
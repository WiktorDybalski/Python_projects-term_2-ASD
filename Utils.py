def turn_into_array(G):
    n = len(G)
    new = [[] for _ in range(n)]
    for i in range(n):
        for v in G[i]:
            new[i].append(v)
    return new


def flip_edges(G):
    n = len(G)
    new = [[] for _ in range(n)]
    for i in range(n):
        for v in G[i]:
            new[v].append(i)
    return new


def add_v_specific(E, S):
    n = len(S)
    for i in range(1, n):
        first = S[i - 1]
        second = S[i]
        E[first].append([second, 0])
        E[second].append([first, 0])
    return E


def add_v(E, first, second):
    n = len(E)
    E[first].append(second)
    E[second].append(first)
    return E


def add_v(E, first, second):
    n = len(E)
    E[first].append(second)
    E[second].append(first)
    return E


def remove_in_directed(Graph, v1, v2):
    Graph = Graph[v1].remove(v2)
    return Graph


def remove(Graph, v1, v2):
    Graph = Graph[v1].remove(v2)
    Graph = Graph[v2].remove(v1)
    return Graph


def reverse_edges(Graph):
    n = len(Graph)
    new = [[] for _ in range(n)]
    for i in range(n):
        for v in Graph[i]:
            new[v].append(i)
    return new


def change_v_and_w(Graph):
    n = len(Graph)
    new = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(Graph[i])):
            v = Graph[i][j][0]
            w = Graph[i][j][1]
            new[i].append([w, v])
    return new



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
    return visited


def is_connected(Graph):
    n = len(Graph)
    visited = BFS(Graph, 0)
    for i in range(n):
        if not visited[i]:
            return False
    return True


def BFS_modd_to_cycle(G, s, t):
    n = len(G)
    visited = [False] * n
    d = [-1] * n
    parrent = [None] * n
    queue = []

    queue.append(s)
    visited[s] = True
    d[s] = 0
    parrent[0] = None

    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if parrent[u] != v and d[v] != -1:
                return True
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                d[v] = d[u] + 1
                parrent[v] = u
    return False


def has_cycle(Graph, s, t):
    cycle = BFS_modd_to_cycle(Graph, s, t)
    return cycle


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


Graph = [[1],
         [0, 2],
         [1, 3, 4],
         [2],
         [2]]

Graph2 = [[1, 2],
          [0, 4],
          [0, 3, 5],
          [2, 4],
          [1, 3],
          [2]]

print(has_cycle(Graph, 0, 6))

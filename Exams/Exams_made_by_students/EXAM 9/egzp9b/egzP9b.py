from egzP9btesty import runtests


def remove_roads(G, R):
    nr = len(R)
    for i in range(nr):
        for v in R[i]:
            if v in G[i]:
                G[i].remove(v)
    return G


def remove(Graph, v1, v2):
    Graph[v1].remove(v2)
    return Graph


def Euler_cycle_iter(G, s):
    stack = [s]
    n = len(G)
    cycle = []
    visited = [False] * n
    parent = [None] * n
    for v in range(n):
        if not visited[v]:
            while stack:
                u = stack[len(stack) - 1]
                visited[u] = True
                for v in G[u]:
                    parent[v] = u
                    stack.append(v)
                    remove(G, u, v)
                    u = v
                    break
                if len(G[u]) == 0:
                    cycle.append(stack.pop(len(stack) - 1))
    cycle = cycle[::-1]
    return cycle


# def Euler_cycle(G):
#     cycle = []
#
#     def DFS_Visit(G, u):
#         nonlocal time, cycle
#         time += 1
#         visited[u] = True
#         for v in G[u]:
#             parent[v] = u
#             remove(G, u, v)
#             DFS_Visit(G, v)
#         cycle.append(u)
#         time += 1
#
#     n = len(G)
#     visited = [False] * n
#     parent = [None] * n
#     time = 0
#     for v in range(n):
#         if not visited[v]:
#             DFS_Visit(G, v)
#     cycle = cycle[::-1]
#     return cycle


def dyrektor(G, R):
    G = remove_roads(G, R)
    route = Euler_cycle_iter(G, 0)
    return route


runtests(dyrektor, all_tests=True)

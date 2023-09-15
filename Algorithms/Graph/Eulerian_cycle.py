# Eulerian Cycle using DFS
# Complexity: O(V + E) for adjacency list or nlogn where n is number of edges

def is_cycle_euler(Graph):
    n = len(Graph)
    for i in range(n):
        cnt = 0
        for v in Graph[i]:
            cnt += 1
        if cnt % 2 == 1:
            return False
    return True


def remove(Graph, v1, v2):
    Graph[v1].remove(v2)
    Graph[v2].remove(v1)
    return Graph


def Euler_cycle(G):
    if is_cycle_euler(G):
        cycle = []

        def DFS_Visit(G, u):
            nonlocal time, cycle
            time += 1
            visited[u] = True
            for v in G[u]:
                if not parent[u] == v:
                    parent[v] = u
                    remove(G, u, v)
                    DFS_Visit(G, v)
                cycle.append(u)
            time += 1

        n = len(G)
        visited = [False] * n
        parent = [None] * n
        time = 0
        for v in range(n):
            if not visited[v]:
                DFS_Visit(G, v)
        cycle = cycle[::-1]
        cycle.append(cycle[0])
        return cycle
    else:
        return None


# Complexity: O(V + E) for adjacency list
def Euler_Circuit_Finder(G):
    visited_edges = []
    num_neighbour = [0 for i in range(len(G))]
    Euler = []
    DFS(G, visited_edges, Euler, num_neighbour)

    return Euler


def explore(graph, node, visited_edges, Euler, num_neighbour):
    global time
    time += 1  # wierzchołek został odwiedzony i time to czas odwiedzenia
    for neighbour in graph[node][num_neighbour[node]:]:
        if (neighbour, node) not in visited_edges and (node, neighbour) not in visited_edges:
            visited_edges.append((neighbour, node))
            visited_edges.append((node, neighbour))
            num_neighbour[node] += 1
            explore(graph, neighbour, visited_edges, Euler, num_neighbour)
    time += 1  # wierzchołek został przetworzony i time to czas przetworzenia
    Euler.append(node)


def DFS(graph, visited_edges, Euler, num_neighbour):
    global time
    time = 0
    v = 0
    explore(graph, v, visited_edges, Euler, num_neighbour)


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


Graph = [[1, 2],
         [0, 2, 3, 4, 5, 6],
         [0, 1, 3, 4, 5, 6],
         [1, 2, 4, 5],
         [1, 2, 3, 5],
         [1, 2, 3, 4],
         [1, 2]]

# print(Euler_cycle(Graph))
a = Euler_Circuit_Finder(Graph)
print(a)

# Dany jest graf nieskierowany G = (V, E) oraz dwa wierzchołki s, t ∈ V . Proszę zaproponować i
# zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie
# z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź). Algorytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego
# poprawność i oszacować złożoność obliczeniową.
# Algorytm należy zaimplementować jako funkcję:
# def longer(G, s, t):
# ...
# która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą
# warunki zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list
# sąsiadów, t.j. G[i] to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0.
# Funkcja powinna zwrócić krotkę zawierającą numery dwóch wierzchołków pomiędzy którymi jest
# krawędź spełniająca warunki zadania, lub None jeśli takiej krawędzi nie ma. Jeśli w grafie oryginalnie
# nie było ścieżki z s do t to funkcja powinna zwrócić None.
# Przykład. Dla argumentów:
# G = [ [1, 2],
# [0, 2],
# [0, 1] ]
# s = 0
# t = 2
# wynikiem jest np. krotka: (0, 2)

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


def BFS(G, s, t):
    n = len(G)
    visited = [False] * n
    d = [0] * n
    parrent = [None] * n
    queue = []

    queue.append(s)
    visited[s] = True
    d[s] = 0
    parrent[0] = None

    while queue:
        u = queue.pop(0)

        for v in G[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                d[v] = d[u] + 1
                parrent[v] = u
    if d[t] == -1:
        d[t] = 1000000000000000000000
        return [parrent, d[t]]
    return [parrent, d[t]]


def remove_edge(G, edge):
    n = len(G)
    v1 = edge[0]
    v2 = edge[1]
    for i in range(n):
        if G[v1][i] == v2:
            G[v1].pop(i)
            break
    for j in range(n):
        if G[v2][j] == v1:
            G[v2].pop(j)
            break
    return G


def add_edge(G, edge):
    v1 = edge[0]
    v2 = edge[1]
    G[v1].append(v2)
    G[v2].append(v1)
    quick_sort(G[v1], 0, len(G[v1]) - 1)
    quick_sort(G[v2], 0, len(G[v2]) - 1)
    return G


def longer(G, s, t):
    n = len(G)
    result = BFS(G, s, t)
    len_of_path = result[1]
    if not len_of_path:
        return None
    the_shortest_path = []
    the_shortest_path.append(t)
    temp = t

    for i in range(len_of_path):
        the_shortest_path.append(result[0][temp])
        temp = result[0][temp]
    for j in range(0, len_of_path):
        edge = [the_shortest_path[j], the_shortest_path[j + 1]]
        G = remove_edge(G, edge)
        new_path = BFS(G, s, t)
        if new_path[1] != len_of_path:
            return (edge[0], edge[1])
        G = add_edge(G, edge)
    return None

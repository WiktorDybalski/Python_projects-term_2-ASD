# Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
# Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
# na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
# opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
# transportu na inny oraz minimalizuje koszt podróży.
# Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
# oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
# zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
# nie istnieje, funkcja powinna zwrócić wartość None.
# Przykład Dla tablicy
# G1 = [ [0,5,1,8,0,0,0 ],
# [5,0,0,1,0,8,0 ],
# [1,0,0,8,0,0,8 ],
# [8,1,8,0,5,0,1 ],
# [0,0,0,5,0,1,0 ],
# [0,8,0,0,1,0,5 ],
# [0,0,8,1,0,5,0 ] ]
# funkcja islands(G1, 5, 2) powinna zwrócić wartość 13
import heapq

from zad1testy import runtests


def add_v_wages(E, first, second, wage):
    n = len(E)
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


def change_v_and_w(Graph):
    n = len(Graph)
    new = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(Graph[i])):
            v = Graph[i][j][0]
            w = Graph[i][j][1]
            new[i].append([w, v])
    return new


def relax(G, u, v, d, parent, visited, w):
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        parent[v] = u


def dijkstry(G, s, t):
    n = len(G)
    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    d[s] = 0
    visited = [False for _ in range(n)]
    pq = [(0, s)]
    while pq:
        curr_d, u = heapq.heappop(pq)
        for w, v in G[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))
            relax(G, u, v, d, parent, visited, w)
        visited[u] = True
    return d[t]


def islands(G, A, B):
    G = matrix_to_adjacency_wages(G)
    G = change_v_and_w(G)
    result = dijkstry(G, A, B)
    return result


runtests(islands)

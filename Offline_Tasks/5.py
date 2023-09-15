# Układ planetarny Algon składa się z n planet o numerach od 0 do n−1. Niestety własności fizyczne układu powodują, że nie da się łatwo przelecieć między dowolnymi
# dwiema planetami. Na szczęście mozolna eksploracja kosmosu doprowadziła do stworzenia listy E dopuszczalnych bezpośrednich przelotów. Każdy element listy E to trójka
# postaci (u, v, t), gdzie u i v to numery planet (można założyć, że u < v) a t to czas podróży między nimi (przelot z u do v trwa tyle samo co z v do u).
# Dodatkową nietypową własnością układu Algon jest to, że niektóre planety znajdują się w okolicy osobliwości. Znajdując się przy takiej planecie możliwe jest zagięcie
# czasoprzestrzeni umożliwiające przedostanie się do dowolnej innej planety leżącej przy osobliwości w czasie zerowym. Zadanie polega na zaimplementowaniu funkcji:
# def spacetravel( n, E, S, a, b ) która zwraca najkrótszy czas podróży z planety a do planety b, mając do dyspozycji listę możliwych bezpośrednich przelotów E
# oraz listę S planet znajdujących się koło osobliwości. Jeśli trasa nie istnieje, to funkcja powinna zwrócić None.
# Rozważmy następujące dane:
# E = [(0,1, 5),
# (1,2,21),
# (1,3, 1),
# (2,4, 7),
# (3,4,13),
# (3,5,16),
# (4,6, 4),
# (5,6, 1)]
# S = [ 0, 2, 3 ]
# a = 1
# b = 5
# n = 7
# wywołanie startravel(n, E, S, a, b) powinno zwrócić liczbę 13. Odwiedzamy po kolei planety 1, 3, 2, 4, 6 i kończymy na planecie 5 (z planety 2 do 3 dostajemy się przez
# zagięcie czasoprzestrzeni). Gdyby a = 1 a b = 2 to wynikiem byłby czas przelotu 1.

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


def add_v(E, S):
    n = len(S)
    for i in range(1, n):
        first = S[i - 1]
        second = S[i]
        E[first].append([second, 0])
        E[second].append([first, 0])
    return E


def dijkstra(n, G, S, a, b):
    distances = [float('inf')] * n
    distances[a] = 0
    visited = [False] * n
    pq = [(0, a)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if visited[current_vertex]:
            continue
        visited[current_vertex] = True
        if current_vertex == b and distances[b] != float('inf'):
            return distances[b]
        for neighbor, weight in G[current_vertex]:
            if visited[neighbor]:
                continue
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return None


def spacetravel(n, E, S, a, b):
    E = edges_to_adjacency_wages(E)
    E = add_v(E, S)
    the_shortest_path = dijkstra(n, E, S, a, b)
    return the_shortest_path

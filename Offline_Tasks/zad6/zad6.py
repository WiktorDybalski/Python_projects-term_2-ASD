# Wiktor Dybalski
# Na początku algorytm przekształca maszyny oraz pracowników jako oddzielnie wierzchołki(każdy pracownik oraz maszyna ma
# swój indywidualny numer). Następnie zmodyfikowany algorytm dfs zwraca boolean czy udało się znaleźć skojarzenie dla
# dla poszczególnej maszyny. Jeśli udało się skojrzenie zapisywane jest w tablicy match oraz zwięszkana jest wartość
# max_matching, jeśli nie to dfs cofa się do wcześniejszej maszyny i sprawdza czy da się przypisać tej maszynie inny
# wierzchołek.
# Złożoność to w przybliżeniu: O(V * E)

from zad6testy import runtests


def dfs_modd(graph, u, visited, match):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            if match[v] == -1 or dfs_modd(graph, match[v], visited, match):
                match[v] = u
                return True
    return False


def binworker(M):
    n = len(M)
    graph = [[] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for machine in M[i]:
            cnt += 1
            graph[i].append(machine + n)

    match = [-1] * cnt
    max_matching = 0

    for i in range(n):
        visited = [False] * cnt
        if dfs_modd(graph, i, visited, match):
            max_matching += 1
    return max_matching

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = False )

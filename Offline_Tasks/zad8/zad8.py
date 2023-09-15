# Wiktor Dybalski
# Program na początku rekurencyjnie przeszukuje ilość ropy w danym miejscu a następnie zapisuję ją do tablicy stations.
# Następnie program przechodzi przez pierwszy wiersz tablicy T oraz przy pomocy tablicy missed sprawdza on najmniejszą
# możliwą ilość zatrzymań w danym przypadku idąc po kolei od punktu do punktu w którym jest ropa.
# Złożoność tego algorytmu to około: O(n * m + m + m log m)
import heapq

from zad8testy import runtests


def find(T, i, j, visited):
    m = len(T[0])
    n = len(T)
    if n - 1 >= i >= 0 and m - 1 >= j >= 0:
        if T[i][j] == 0 or visited[i][j]:
            return 0
        else:
            visited[i][j] = True
            return T[i][j] + find(T, i + 1, j, visited) + find(T, i, j + 1, visited) + find(T, i - 1, j, visited) \
                + find(T, i, j - 1, visited)
    else:
        return 0


def plan(T):
    m = len(T[0])
    n = len(T)
    i = 0
    stations = []
    missed = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    for j in range(m):
        if T[0][j] != 0:
            stations.append([j, find(T, i, j, visited)])
    if not T[0][m - 1]:
        stations.append([m - 1, 0])
    fuel = stations[0][1]
    stations.pop(0)
    cnt = 1
    prev = 0
    for station, oil in stations:
        dis = station - prev
        heapq.heappush(missed, -oil)
        if fuel >= dis:
            prev = station
            fuel -= dis
            continue
        while fuel < dis and missed:
            fuel += -heapq.heappop(missed)
            cnt += 1
    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)

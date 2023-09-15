# Wiktor Dybalski
# Program wykorzystuje technikę programowania dynamicznego do obliczania wyniku.
# W tablicy d przechowywana jest największa liczba komnat, jaką można odwiedzić kończąc ruch na danym polu.
# Bardzo duża ujemna wartość oznacza, iż miejsce jest nieosiągalne. Zauważyłem, że jednym z bardziej sensownych
# rozwiązań będzie poruszanie się w górę oraz w dół, a następnie gdy nie można się ruszyć, należy przesunąć się w prawo.
# Program rozwiązuje problem największej odległości w danym miejscu wracając kolejną pętlą z dołu do góry, nadpisując
# kolejno najwięszką możliwość odległość od punktu startowego.
# Złożoność programu to: O(n^2)

from zad7testy import runtests


def maze(L):
    wiersze = len(L)
    kolumny = len(L[0])
    if L[0][0] == '#':
        return -1
    d = [[-100 * 188 for x in range(kolumny)] for y in range(wiersze)]
    d[0][0] = 0
    for u in range(1, wiersze):
        if L[u][0] == '#':
            break
        d[u][0] = d[u - 1][0] + 1
    for i in range(1, kolumny):
        temp = -10 ** 18
        for u in range(0, wiersze):
            if L[u][i] == '#':
                temp = -10 ** 18
            else:
                temp = max(temp, d[u][i - 1])
                temp += 1
                d[u][i] = max(d[u][i], temp)
        temp = -10 ** 18
        for u in reversed(range(0, wiersze)):
            if L[u][i] == '#':
                temp = -10 ** 18
            else:
                temp = max(temp, d[u][i - 1])
                temp += 1
                d[u][i] = max(d[u][i], temp)
    if d[wiersze - 1][kolumny - 1] < 0:
        return -1
    else:
        return d[wiersze - 1][kolumny - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)

# Wiktor Dybalski
# Algorytm dynamicznie rozwiązuje przedstawiony problem. Tworzy tablicę dp w której zapisuje wynik funkcji
# f(i, j) czyli sumy odległości biurowców z pozycji od X[0] do X[i] dla działek od Y[0] do Y[j].
# Algorytm używa funkcji min w warunku j - i > 0 aby uniknąć przechodzenia po całym wierszu tablicu co poprawia
# lekko wydajność algorytmu. Funkcja zwraca minimum aby wybrać najlepszy możliwy przypadek w tym zadaniu
# Złożoność algorytmu: O(n * m^2)

from egz2btesty import runtests


def substraction(x, y):
    if x - y > 0:
        return x - y
    return y - x


def parking(X, Y):
    inf = float("inf")
    offices = len(X)
    lands = len(Y)
    dp = [[inf for _ in range(lands)] for _ in range(offices)]
    for i in range(lands):
        dp[0][i] = substraction(X[0], Y[i])
    for i in range(1, offices):
        for j in range(lands):
            if j - i < 0:
                continue
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + substraction(X[i], Y[j])
            else:
                x = min(dp[i - 1][:j])
                dp[i][j] = substraction(X[i], Y[j]) + x
    result = min(dp[offices - 1])
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)

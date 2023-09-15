# Wiktor Dybalski
# Przedstawiony algorytm sortuje tablice P po wartości x, następnie odwraca tablice co powoduje ze mamy
# największą wartość x na początku. Następnie sprawdza po kolei każdy punkt z następnym, kolejnym. Nie musi
# sprawdzać wszystkich ze wszystkimi gdyż posortowania po X nierosnąco rozwiązuje problem że wcześniejszy wierzchołek
# może zostać zdominowany przez póżniejszy.
# Złożoność: O(n^2)
from egz2atesty import runtests


def dominance(P):
    P = sorted(P)
    P = P[::-1]
    the_best = 0
    n = len(P)
    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
                cnt += 1
        the_best = max(cnt, the_best)
    return the_best


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance, all_tests=True)

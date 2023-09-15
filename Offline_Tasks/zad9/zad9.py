import heapq

from zad9testy import runtests

# Za każdym razem aktualizuję, czy jadąc z aktualnego parkingu można poprawić czas z wyjątkiem i bez wyjątku

from zad9testy import runtests


def sus(x):
    return x[0]


def min_cost(O, C, T, L):
    inf = float('inf')
    n = len(O)
    print("ilosc parkingow:", n)
    tab = [None for _ in range(n + 1)]
    tab[0] = [0, 0, 0, 0]
    for i in range(n):
        tab[i + 1] = [O[i], C[i], inf, inf]
    tab.sort(key=sus)
    n += 1

    # tab[i] = [odległosć, cena, min cena bez wyjatku, min cena z wyjatkiem]
    wynik = inf

    for i in range(n):

        dist = tab[i][0]
        parking = tab[i][1]
        cost = tab[i][2] + parking
        cost2 = tab[i][3] + parking

        if dist + T >= L and cost < wynik:
            wynik = cost

        if dist + T >= L and cost2 < wynik:
            wynik = cost2

        if dist + 2 * T >= L and cost < wynik:
            wynik = cost

        for k in range(i + 1, n):

            new_dist = tab[k][0]
            min_cost = tab[k][2]
            min_cost2 = tab[k][3]

            if dist + T >= new_dist:

                if cost < min_cost:

                    min_cost = cost
                    tab[k][2] = min_cost

                    if cost <= min_cost2:
                        min_cost2 = cost
                        tab[k][3] = min_cost2

                if cost2 < min_cost2:
                    min_cost2 = cost2
                    tab[k][3] = min_cost2

            elif dist + 2 * T >= new_dist:

                if cost < min_cost2:
                    min_cost2 = cost
                    tab[k][3] = min_cost2

            else:
                break

    return wynik


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=False)

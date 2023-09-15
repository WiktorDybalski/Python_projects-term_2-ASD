from egz1atesty import runtests

t = [6, 7, 3, 4, 1]


def snow(S):
    S = sorted(S)
    S = S[::-1]
    n = len(S)
    day = 0
    sum = 0
    while day < n and S[day] - day > 0:
        sum += S[day] - day
        day += 1
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)

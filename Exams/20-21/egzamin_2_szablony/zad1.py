from zad1testy import runtests


def has_mutual_point(x, y):
    if x[1] == x[0]:
        return True
    return False


def create_summ(x, y):
    first = min(x[0], y[0])
    second = max(x[1], y[1])
    return first, second


def intuse(I, x, y):
    I = sorted(I, key=lambda x: x[1])
    I = sorted(I, key=lambda x: x[0])
    n = len(I)
    new_I = [(I[i], i) for i in range(n)]
    for i in range(n):
        j = 0
        new_n = len(new_I)
        while j <= i:
            if I[i][1] == I[j][0]:
                first = min(I[i][0], I[j][0])
                second = max(I[i][1], I[j][1])
                new_I.append(first, second, new_n)
            j += 1

    return []


runtests(intuse)

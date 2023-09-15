# Find the longest possible route in a matrix

def print_tab(d):
    n = len(d)
    for i in range(n):
        print(d[i])


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


L = ['....', '....', '....', '....']
R = ['......', '#..#..', '.#..#.', '##..#.', '......', '......']
print(maze(L))

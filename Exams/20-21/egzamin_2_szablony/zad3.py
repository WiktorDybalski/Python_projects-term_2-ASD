from zad3testy import runtests


def lamps(n, T):
    lampss = ['G'] * n
    cnt = 0
    the_best = 0
    for j in range(len(T)):
        start = T[j][0]
        end = T[j][1]
        the_best = max(cnt, the_best)
        for i in range(n):
            if i > end:
                break
            if end >= i >= start:
                if lampss[i] == 'G':
                    lampss[i] = 'R'
                elif lampss[i] == 'R':
                    lampss[i] = 'B'
                    cnt += 1
                else:
                    lampss[i] = 'G'
                    cnt -= 1
        the_best = max(cnt, the_best)
    return the_best


runtests(lamps)

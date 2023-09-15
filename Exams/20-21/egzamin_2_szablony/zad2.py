from zad2testy import runtests


class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []
        self.W = 0

    def addEdge(self, x, w, id):  # dodaj krawędź z tego węzła do węzła x
        self.edges.append(x)  # o wadze w i identyfikatorze id
        self.weights.append(w)
        self.ids.append(id)


def rek(u, w, j, tab):
    res = 0
    for i in range(len(u.edges)):
        res += rek(u.edges[i], u.weights[i], u.ids[i], tab)
    u.w = (res + w)
    tab.append((res + w, j))
    return w + res


def balance(T):
    Tab = []
    rek(T, 0, 0, Tab)
    n = len(Tab)
    top = Tab[n - 1][0]
    mini = float('inf')
    index = None
    for i in range(n - 1):
        if top - Tab[i][0] < mini:
            mini = top - Tab[i][0]
            index = Tab[i][1]
    return index


runtests(balance)

# Find and Union
# Complexity Find: O(log n)
# Complexity Union: O(log n)
# Complexity Find + Union, n operations for m elements: O(m * logm) - logarytm iterowany
class Node():
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


# Find and Union as an array

def find(v, parent, rank):
    while parent[v] != v:
        v = parent[v]
    return v


def union(u, v, parent, rank):
    x = find(u, parent, rank)
    y = find(v, parent, rank)
    if rank[x] > rank[y]:
        parent[y] = x
        return x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1
        return y

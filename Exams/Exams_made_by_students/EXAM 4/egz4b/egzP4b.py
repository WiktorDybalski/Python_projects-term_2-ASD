from egzP4btesty import runtests


class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None


def max(root):
    while root.right is not None:
        root = root.right
    return root.key


def min(root):
    while root.left is not None:
        root = root.left
    return root.key


def prev(x):
    if x.left is not None:
        x = x.left
        while x.right is not None:
            x = x.right
        return x
    else:
        while x.parent.left == x:
            x = x.parent
        if x.parent.right == x:
            x = x.parent
            return x


def next(x):
    if x.right is not None:
        x = x.right
        while x.left is not None:
            x = x.left
        return x
    else:
        while x.parent.right == x:
            x = x.parent
        if x.parent.left == x:
            x = x.parent
            return x


def sol(root, T):
    n = len(T)
    sum = 0
    minimum = min(root)
    maximum = max(root)
    for i in range(n):
        if T[i].key == minimum or T[i].key == maximum:
            continue
        else:
            val = T[i].key
            first = prev(T[i]).key
            second = next(T[i]).key
            if (first + second) == val * 2:
                sum += val
    return sum


runtests(sol, all_tests=True)

def create_tree_of_sum(T):
    n = len(T)
    temp = n
    amount = 1 + temp
    while temp > 1:
        amount += (temp + 1) // 2
        temp = (temp + 1) // 2
    new_T = [0] * amount
    for i in range(n - 1, -1, -1):
        new_T[i + amount - n] = T[i]
    index = parent(new_T, amount - 1)
    for i in range(index, -1, -1):
        if left(new_T, i) < amount:
            new_T[i] += new_T[left(new_T, i)]
        if right(new_T, i) < amount:
            new_T[i] += new_T[right(new_T, i)]
    return new_T


def parent(T, x):
    return (x - 1) // 2


def left(T, x):
    return 2 * x + 1


def right(T, x):
    return 2 * x + 2


def update(i, x):
    pass


def explore(tree_of_sum, T, i, j):
    n = len(T)


def sum(T, i, j):
    tree_of_sum = create_tree_of_sum(T)
    sum = explore(tree_of_sum, T, i, j)


T = [0, 7, 5, 3, 1, 8, 6, 12, 3]
n = len(T)
print(sum(T, 0, n - 1))

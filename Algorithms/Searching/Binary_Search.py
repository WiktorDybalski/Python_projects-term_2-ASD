# Binary_Search for an array

tab = [2, 4, 5, 7, 9, 17, 155, 167, 1677, 24242, 24242441]


def Binary_Search(tab, x):
    n = len(tab)
    L = 0
    R = n - 1
    if tab[L] == x:
        return L
    if tab[R] == x:
        return R

    while L <= R:
        mid = (L + R) // 2
        if tab[mid] == x:
            return mid
        if tab[mid] < x:
            L = mid
        else:
            R = mid


array = [2, 1, 4, 3, 1, 5, 2, 7, 3, 8]
x = max(array)
print(x, "is on the index: ", Binary_Search(array, x))

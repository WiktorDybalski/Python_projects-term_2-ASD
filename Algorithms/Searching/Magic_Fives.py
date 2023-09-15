# Szukamy liczby, która po posortowaniu byłaby na pozycji k

A = [6, 3, 8, 9, 3, 2, 4, 7]
k = 5


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def med5(A, p, r):
    if r - p < 5:
        return sorted(A[p:r + 1])[len(A[p:r + 1]) // 2]
    medians = []
    for i in range(p, r + 1, 5):
        medians.append(med5(A, i, min(i + 4, r)))
    return med5(medians, 0, len(medians) - 1)


def magic_fives(A, i):
    if len(A) == 1:
        return A[0]
    pivot = med5(A, 0, len(A) - 1)
    left = []
    middle = []
    right = []
    for elem in A:
        if elem < pivot:
            left.append(elem)
        elif elem == pivot:
            middle.append(elem)
        else:
            right.append(elem)
    if i < len(left):
        return magic_fives(left, i)
    elif i < len(left) + len(middle):
        return pivot
    else:
        return magic_fives(right, i - len(left) - len(middle))


print(magic_fives(A, k))

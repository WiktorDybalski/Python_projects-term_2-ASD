# QuickSort for an array

array = [3, 6, 2, 1, 5, 9, 8, 7, 4]
n = len(array)


# Quick_Sort for an array
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        p = q + 1
    return A


# Quick_Sort for an array by i index(with wages)
def partition(A, p, r, index):
    x = A[r][index]
    i = p - 1
    for j in range(p, r):
        if A[j][index] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort_for_i_index(A, p, r, i):
    while p < r:
        q = partition(A, p, r)
        quick_sort_for_i_index(A, p, q - 1, i)
        p = q + 1
    return A


print(array)
quick_sort(array, 0, n - 1)
print(array)

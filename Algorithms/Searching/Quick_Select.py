# Complexity for perfect divided: O(n)

T = [5, 2, 6, 1, 6, 8, 2, 4, 1, 4, 6, 12, 7, 2]


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def Quick_Select(T, p, r, k):
    x = partition(T, p, r)
    if x == k:
        return T[x]
    if x > k:
        return Quick_Select(T, p, x - 1, k)
    if x < k:
        return Quick_Select(T, x + 1, r, k)


print(T)
print(T[5])
print(Quick_Select(T, 0, len(T) - 1, 5))
print(Quick_Select(T, 0, len(T) - 1, 9))
print(T)
T = sorted(T)
print(T)

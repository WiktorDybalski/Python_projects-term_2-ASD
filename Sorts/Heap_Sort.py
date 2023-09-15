# Heap_Sort
# Complexity: O(nlogn)

def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parrent(i):
    return (i - 1) // 2


def build_heap(A):
    n = len(A)
    for i in range(parrent(n - 1), -1, - 1):
        heapify(A, i, n)


def heapify(A, i, n):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)


def Heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)


T = [3, 6, 2, 8, 3, 9, 7, 1, 10, 5]
print(T)
Heap_sort(T)
print(T)

# def insert(tab, x):
#     tab.append(x)
#     i = len(tab) - 1
#     while (parrent(i) >= 0) and tab[i] > tab[parrent(i)]:
#         tab[parrent(i)], tab[i] = tab[i], tab[parrent(i)]
#         i = parrent(i)

# def merge(S):
#     build_heap(S)
#     war = Node(-1)
#     kon = war
#     while S:
#         kon.next = S[0]
#         S[0] = S[0].next
#         kon = kon.next
#         kon.next = None
#         S[0], S[-1] = S[-1], S[0]
#         if S[-1] == None:
#             S.pop()
#             heapify(S)
#     return war.next

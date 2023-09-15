# MergeSort for arrays

array = [5, 2, 6, 1, 6, 8, 2, 4, 1, 4, 6, 12, 7, 2]


def MergeSort(T):
    n = len(T)
    if n > 1:
        n //= 2
        L = T[:n]
        R = T[n:]

        MergeSort(L)
        MergeSort(R)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            T[k] = R[j]
            j += 1
            k += 1
        return T


print(array)
print(MergeSort(array))


# MergeSort for linked list

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def merge(L1, L2):
    merged = Node("#")
    copy = merged
    while L1 and L2:
        if L1.val < L2.val:
            merged.next = L1
            merged = merged.next
            L1 = L1.next
        else:
            merged.next = L2
            merged = merged.next
            L2 = L2.next
    while L1:
        merged.next = L1
        merged = merged.next
        L1 = L1.next
    while L2:
        merged.next = L2
        merged = merged.next
        L2 = L2.next
    return copy.next


def get_mid(L):
    slow, fast = L, L.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergesort(L):
    if not L or not L.next:
        return L
    left = L
    right = get_mid(L)
    tmp = right.next
    right.next = None
    right = tmp
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


def print_linked_list(a):
    print(a.val, end="=>")
    while a.next is not None:
        print(a.next.val, end="=>")
        a = a.next


e = Node(2)
d = Node(8, e)
c = Node(9, d)
b = Node(3, c)
a = Node(4, b)

print_linked_list(a)
print(" ")
print("---------")
print_linked_list(mergesort(a))

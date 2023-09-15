# Bubble_sort_for_array
tab1 = [0, 3, 2, 1, 5, 8, 3, 5, 7, 9]
tab2 = [11, 3, 2, 1, 5, 8, 3, 5, 7, 9]


def Bubble_Sort(a):
    n = len(a)
    change = True
    x = -1
    cnt = 0
    while change:
        x += 1
        change = False
        for i in range(n - x - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                change = True
        cnt += 1
    return cnt


print(tab1)
print(Bubble_Sort(tab1))

print(tab1)


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def create_linked_list(T):
    if len(T) > 0:
        g = Node(T[0])
        for i in range(1, len(T)):
            linked_insert_at_the_end(g, T[i])
    return g


def linked_insert_at_the_end(g, val):
    cur = g
    while cur.next is not None:
        cur = cur.next
    cur.next = Node(val)


# Bubble sort for linked list

def length_list(g):
    temp = g
    counter = 0
    while temp is not None:
        counter += 1
        temp = temp.next
    return counter


def sort2(p):
    g = p
    if p.next is None:
        return g
    if p.next.next is None:
        return g
    x = -1
    for i in range(length_list(g) - x):
        x += 1
        while p.next.next is not None:
            first = p.next
            second = p.next.next

            if second.val < first.val:
                temp = first
                p.next = p.next.next
                temp.next = second.next
                second.next = temp
            p = p.next
        p = g
    return g


g = Node(2)
f = Node(9, g)
e = Node(5, f)
d = Node(2, e)
c = Node(8, d)
b = Node(3, c)
a = Node(6, b)
g = Node(1, a)


def print_linked_list(g):
    while g is not None:
        print(g.val, end=" => ")
        g = g.next


print_linked_list(g)
print("-------")
print_linked_list(sort2(g))

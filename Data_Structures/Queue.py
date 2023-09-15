# Queue by Node implementation

from WDI.utils import linked_print_all_with_guardian


class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def push(g, x):
    while g.next is not None:
        g = g.next
    new = Node(x)
    g.next = new


def pop(g):
    temp = g.next
    g.next = g.next.next
    return temp


def is_Empty(g):
    if g.next is None:
        return True
    return False


g = Node(0)
push(g, 7)
push(g, 4)
push(g, 3)
linked_print_all_with_guardian(g)
pop(g)
linked_print_all_with_guardian(g)
pop(g)
linked_print_all_with_guardian(g)

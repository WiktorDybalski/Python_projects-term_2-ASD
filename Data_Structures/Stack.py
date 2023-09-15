from WDI.utils import linked_print_all


# Node implementation

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


global top


def l_pop(g):
    if g.next is None:
        return None
    else:
        temp = g.next
        g.next = g.next.next
    return temp


def l_push(g, x):
    if g.next is None:
        top = Node(x)
        g.next = top
    else:
        new = Node(x)
        temp = g.next
        top = new
        top.next = temp
        g.next = top


def is_empty(g):
    if g.next is None:
        return True
    return False


g = Node(0)
print(is_empty(g))
linked_print_all(g)
l_push(g, 3)
l_push(g, 8)
l_push(g, 6)
linked_print_all(g)
l_pop(g)
linked_print_all(g)
l_pop(g)
linked_print_all(g)
print(is_empty(g))

# Array Implementation
stack = []
top = 0


def a_push(x):
    stack.append(x)
    global top
    top += 1


def a_pop(stack):
    global top
    if top == -1:
        return None
    else:
        stack.pop()
        top -= 1


def how_many(stack):
    global top
    return top


print(stack)
print(how_many(stack))
a_push(4)
a_push(7)
a_push(2)
print(stack)
print(how_many(stack))
a_pop(stack)
print(stack)
a_pop(stack)
print(how_many(stack))

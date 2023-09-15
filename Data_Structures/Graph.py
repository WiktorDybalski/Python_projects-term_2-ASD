# Graph implementation

from WDI.utils import print_Tab


# Graph representation by List of edges
class Node():
    def __init__(self, val1, val2, next=None):
        self.val1 = val1
        self.val2 = val2
        self.next = next


def put_edge_to_Graph(g, edge):
    temp = g
    while temp.next is not None:
        temp = temp.next
    new = Node(edge[0], edge[1])
    temp.next = new


def linked_print_all_with_guardian(p):
    while p.next is not None:
        print("(", end="")
        print(p.next.val1, end=", ")
        print(p.next.val2, end=") => ")
        p = p.next
    print("")


g = Node(0, 0)
edge1 = [1, 4]
edge2 = [4, 2]
linked_print_all_with_guardian(g)
put_edge_to_Graph(g, edge1)
linked_print_all_with_guardian(g)
put_edge_to_Graph(g, edge2)
linked_print_all_with_guardian(g)

# Graph representation by array
Graph = [(0, 1), (1, 6), (6, 4), (4, 7), (4, 2), (2, 3), (3, 0), (0, 5)]
V = 8
E = 8
size = [V, E]


def create_matrix(Graph, size):
    n = len(Graph)
    matrix = [[0 for _ in range(size[0])] for s in range(size[0])]
    for i in range(n):
        matrix[Graph[i][1]][Graph[i][0]] = 1
        matrix[Graph[i][0]][Graph[i][1]] = 1
        matrix[i][i] = "--"
    print_Tab(matrix)


create_matrix(Graph, size)

# Graph representation by adjacency lists

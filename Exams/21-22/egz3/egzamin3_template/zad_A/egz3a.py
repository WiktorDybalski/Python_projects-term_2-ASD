from egz3atesty import runtests

inf = float('inf')


def snow(T, I):
    n = len(I)
    the_biggest = 0
    for i in range(n):
        the_biggest = max(the_biggest, I[i][1])
    array = [0 for _ in range(the_biggest + 1)]
    for i in range(n):
        start = I[i][0]
        end = I[i][1]
        for j in range(start, end + 1):
            array[j] += 1
    return max(array)


# def change_to_array(compartments):
#     n = len(compartments)
#     array = []
#     for i in range(n):
#         if compartments[i][0] not in array:
#             array.append(compartments[i][0])
#         if compartments[i][1] not in array:
#             array.append(compartments[i][1])
#     array.sort()
#     return array
#
#
# class interval_tree_Node:
#     def __init__(self, left=None, right=None, parent=None, key=None, span=None):
#         self.left = left
#         self.right = right
#         self.parent = parent
#         self.key = key
#         self.span = span
#         self.intervals = []
#
#
# def insert(root, key, span):
#     if root is None:
#         return interval_tree_Node(None, None, root, key, span)
#     if key < root.key:
#         root.left = insert(root.left, key, (root.span[0], root.key))
#         if root.left is not None:
#             root.left.parent = root
#     elif key > root.key:
#         root.right = insert(root.right, key, (root.key, root.span[1]))
#         if root.right is not None:
#             root.right.parent = root
#     return root
#
#
# def print_interval_tree(root):
#     if root is None:
#         return None
#     else:
#         left = print_interval_tree(root.left)
#         if left is not None:
#             print(left)
#         print("key:", root.key, "Span:", root.span, "Intervals:", root.intervals)
#         right = print_interval_tree(root.right)
#         if right is not None:
#             print(right)
#
#
# def create_interval_tree(compartments):
#     inf = float('inf')
#     numbers = change_to_array(compartments)
#     n = len(numbers)
#     root_number = numbers[n // 2]
#     root = interval_tree_Node(None, None, None, root_number, (-inf, inf))
#     root1_number = numbers[(0 + n // 2) // 2]
#     root2_number = numbers[(n // 2 + n) // 2]
#     root.left = interval_tree_Node(None, None, None, root1_number, (-inf, root.key))
#     root.right = interval_tree_Node(None, None, None, root2_number, (root.key, inf))
#     for i in range(n // 2 - 1, -1, -1):
#         if i != (0 + n // 2) // 2:
#             insert(root, numbers[i], None)
#     for i in range(n // 2 + 1, n):
#         if i != (n // 2 + n) // 2:
#             insert(root, numbers[i], None)
#     return root
#
#
# def add_base_points(root):
#     if root.left is None and root.key != "B":
#         root.left = interval_tree_Node(None, None, root, "B", (root.span[0], root.key))
#     if root.right is None and root.key != "B":
#         root.right = interval_tree_Node(None, None, root, "B", (root.key, root.span[1]))
#     if root.left is not None:
#         add_base_points(root.left)
#     if root.right is not None:
#         add_base_points(root.right)
#
#
# def interval_intersection(first, second):
#     if first[1] < second[0] or second[1] < first[0]:
#         return False
#     if first[0] == second[0] and first[1] == second[1]:
#         return first
#     else:
#         return max(first[0], second[0]), min(first[1], second[1])
#
#
# def insert_interval(root, interval):
#     curr_interval = interval_intersection(root.span, interval)
#     if curr_interval is False:
#         return
#     if curr_interval == root.span:
#         root.intervals.append(interval)
#         return
#     if root.left is not None:
#         insert_interval(root.left, interval)
#     if root.right is not None:
#         insert_interval(root.right, interval)
#
#
# def snow(T, I):
#     n = len(I)
#     points = []
#     for k in range(n):
#         if I[k][0] == I[k][1]:
#             points.append(I[k][0])
#     interval_tree = create_interval_tree(I)
#     add_base_points(interval_tree)
#     for i in range(n):
#         insert_interval(interval_tree, I[i])
#     print_interval_tree(interval_tree)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)

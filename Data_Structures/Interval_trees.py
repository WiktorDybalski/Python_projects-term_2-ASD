# Interval_tree structure
# Complexity: O(nlogn)
# Complexity of insert and delete an interval: O(logn)
# Complexity of search intervals that contain a given point: O(nlogn)

compartments = [(0, 10), (5, 20), (7, 12), (10, 15)]
inf = float('inf')


def change_to_array(compartments):
    n = len(compartments)
    array = []
    for i in range(n):
        if compartments[i][0] not in array:
            array.append(compartments[i][0])
        if compartments[i][1] not in array:
            array.append(compartments[i][1])
    array.sort()
    return array


class interval_tree_Node:
    def __init__(self, left=None, right=None, parent=None, key=None, span=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key
        self.span = span
        self.intervals = []


def insert(root, key, span):
    if root is None:
        return interval_tree_Node(None, None, root, key, span)
    if key < root.key:
        root.left = insert(root.left, key, (root.span[0], root.key))
        if root.left is not None:
            root.left.parent = root
    elif key > root.key:
        root.right = insert(root.right, key, (root.key, root.span[1]))
        if root.right is not None:
            root.right.parent = root
    return root


def print_interval_tree(root):
    if root is None:
        return None
    else:
        left = print_interval_tree(root.left)
        if left is not None:
            print(left)
        print("key:", root.key, "Span:", root.span, "Intervals:", root.intervals)
        right = print_interval_tree(root.right)
        if right is not None:
            print(right)


def create_interval_tree(compartments):
    inf = float('inf')
    numbers = change_to_array(compartments)
    n = len(numbers)
    root_number = numbers[n // 2]
    root = interval_tree_Node(None, None, None, root_number, (-inf, inf))
    root1_number = numbers[(0 + n // 2) // 2]
    root2_number = numbers[(n // 2 + n) // 2]
    root.left = interval_tree_Node(None, None, None, root1_number, (-inf, root.key))
    root.right = interval_tree_Node(None, None, None, root2_number, (root.key, inf))
    for i in range(n // 2 - 1, -1, -1):
        if i != (0 + n // 2) // 2:
            insert(root, numbers[i], None)
    for i in range(n // 2 + 1, n):
        if i != (n // 2 + n) // 2:
            insert(root, numbers[i], None)
    return root


def add_base_points(root):
    if root.left is None and root.key != "B":
        root.left = interval_tree_Node(None, None, root, "B", (root.span[0], root.key))
    if root.right is None and root.key != "B":
        root.right = interval_tree_Node(None, None, root, "B", (root.key, root.span[1]))
    if root.left is not None:
        add_base_points(root.left)
    if root.right is not None:
        add_base_points(root.right)


def interval_intersection(first, second):
    if first[1] < second[0] or second[1] < first[0]:
        return False
    if first[0] == second[0] and first[1] == second[1]:
        return first
    else:
        return max(first[0], second[0]), min(first[1], second[1])


def insert_interval(root, interval):
    curr_interval = interval_intersection(root.span, interval)
    if curr_interval is False:
        return
    if curr_interval == root.span:
        root.intervals.append(interval)
        return
    if root.left is not None:
        insert_interval(root.left, interval)
    if root.right is not None:
        insert_interval(root.right, interval)


inverval_tree1 = create_interval_tree(compartments)
add_base_points(inverval_tree1)
insert_interval(inverval_tree1, (7, 20))
print_interval_tree(inverval_tree1)

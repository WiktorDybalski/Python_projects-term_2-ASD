# Binary Search Tree and basic functions
# The average Computational complexity: O(h), h-height of the tree

class BST_Node:
    def __init__(self, left=None, right=None, parent=None, key=None, data=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key
        self.data = data


def print_BST(root):
    if root is None:
        return None
    else:
        left = print_BST(root.left)
        if left is not None:
            print(left)
        print("key:", root.key, "Data:", root.data)
        right = print_BST(root.right)
        if right is not None:
            print(right)


def insert(root, key, data):
    if root is None:
        return BST_Node(None, None, None, key, data)
    if key < root.key:
        root.left = insert(root.left, key, data)
        if root.left is not None:
            root.left.parent = root
    elif key > root.key:
        root.right = insert(root.right, key, data)
        if root.right is not None:
            root.right.parent = root
    else:
        root.data = data
    return root


def delete(root, key):
    to_delete = search(root, key)


def search(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def max(root):
    while root.right is not None:
        root = root.right
    return root.key, root.data


def min(root):
    while root.left is not None:
        root = root.left
    return root.key, root.data


def prev(x):
    if x.left is not None:
        x = x.left
        while x.right is not None:
            x = x.right
        return x
    else:
        while x.parent.left == x:
            x = x.parent
        if x.parent.right == x:
            x = x.parent
            return x


def next(x):
    if x.right is not None:
        x = x.right
        while x.left is not None:
            x = x.left
        return x
    else:
        while x.parent.right == x:
            x = x.parent
        if x.parent.left == x:
            x = x.parent
            return x


root = BST_Node(None, None, None, 20, "20")
print("Drzewo BST:")
print_BST(root)
root = insert(root, 17, "17")
root = insert(root, 5, "5")
root = insert(root, 19, "19")
root = insert(root, 18, "18")
root = insert(root, 3, "3")
root = insert(root, 30, "30")
root = insert(root, 27, "27")
root = insert(root, 40, "40")
root = insert(root, 50, "50")

print("Drzewo BST:")
print_BST(root)
print(min(root))
print(max(root))
print(prev(search(root, 18)))
print(next(search(root, 18)))

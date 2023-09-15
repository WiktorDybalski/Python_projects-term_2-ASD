class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def find_min_max(self):
        if self.head is None:
            return None, None

        current = self.head
        min_val = current.value
        max_val = current.value

        while current is not None:
            if current.value < min_val:
                min_val = current.value
            if current.value > max_val:
                max_val = current.value
            current = current.next

        return min_val, max_val


# przykładowe użycie
my_list = LinkedList()
my_list.add_node(3)
my_list.add_node(8)
my_list.add_node(1)
my_list.add_node(10)
my_list.add_node(5)

min_val, max_val = my_list.find_min_max()

print("Najmniejsza wartość w linked liście to:", min_val)
print("Największa wartość w linked liście to:", max_val)

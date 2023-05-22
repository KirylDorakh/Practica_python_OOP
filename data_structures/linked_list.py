class Node:
    # инициализация
    def __init__(self, cargo=None, next_b=None, prev_b=None):
        self.cargo = cargo
        self.next_b = next_b
        # двусвзяный
        self.prev_b = prev_b

    # вывод
    def __str__(self):
        return str(self.cargo)


# односвязный
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
print(node1)

node1.next_b = node2
node2.next_b = node3
print(node1.next_b)

# двусвязный
node3.prev_b = node2
node2.prev_b = node1
print(node2.prev_b)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_end(self, value):
        new_node = Node(value)

        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_front(self):
        if not self.head:
            return None

        removed_value = self.head.value

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return removed_value

    def remove_from_end(self):
        if not self.tail:
            return None

        removed_value = self.tail.value

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return removed_value

    def print_forward(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values))

    def print_backward(self):
        current = self.tail
        values = []
        while current:
            values.append(str(current.value))
            current = current.prev
        print(" <- ".join(values))


# Cria uma lista duplamente ligada
dll = DoublyLinkedList()

# Caso 1: Adiciona elementos no início
dll.add_to_front(10)
dll.add_to_front(20)
dll.add_to_front(30)
# Lista atual: 30 <-> 20 <-> 10

# Caso 2: Adiciona elementos no final
dll.add_to_end(40)
dll.add_to_end(50)
# Lista atual: 30 <-> 20 <-> 10 <-> 40 <-> 50

# Caso 3: Remove elementos do início
print("Removido do início:", dll.remove_from_front())  # Deve remover 30
print("Removido do início:", dll.remove_from_front())  # Deve remover 20
# Lista atual: 10 <-> 40 <-> 50

# Caso 4: Remove elementos do final
print("Removido do fim:", dll.remove_from_end())  # Deve remover 50
# Lista atual: 10 <-> 40

# Caso 5: Remove todos até esvaziar
print("Removido do início:", dll.remove_from_front())  # 10
print("Removido do início:", dll.remove_from_front())  # 40
print("Removido do início:", dll.remove_from_front())  # None (lista vazia)

dll2 = DoublyLinkedList()

dll2.add_to_front(10)
dll2.add_to_end(20)
dll2.add_to_end(30)
dll2.add_to_front(5)

dll2.print_forward()   # Esperado: 5 -> 10 -> 20 -> 30
dll2.print_backward()  # Esperado: 30 <- 20 <- 10 <- 5

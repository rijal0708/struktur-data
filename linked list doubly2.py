class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        if current is None:
            print("List is empty")
            return

        if current.data == data:
            if current.next:
                current.next.prev = None
            self.head = current.next
            current = None
            return

        while current:
            if current.data == data:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                current = None
                return
            current = current.next

        print("Data not found")

    def display(self):
        current = self.head
        if current is None:
            print("List is empty")
            return

        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Contoh penggunaan:
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append("kuliah")
doubly_linked_list.append("struktur data")
doubly_linked_list.append("sesi 40")
doubly_linked_list.display()  

doubly_linked_list.prepend("struktur data")
doubly_linked_list.display()  

doubly_linked_list.delete("estetika humanisme")
doubly_linked_list.display()  

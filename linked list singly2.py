class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer ke node berikutnya

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Kepala (head) dari linked list

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        if current is None:
            print("List is empty")
            return

        if current.data == data:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print("Data not found")
            return

        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        if current is None:
            print("List is empty")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Contoh penggunaan:  mengunakan singlylinkedlist
linked_list = SinglyLinkedList()
linked_list.append("kuliah")
linked_list.append("struktur data")
linked_list.append("sesi 20")
linked_list.display()  

linked_list.prepend("my data")
linked_list.display()  

linked_list.delete("sesi 20")
linked_list.display()  

linked_list.delete("basis data")  

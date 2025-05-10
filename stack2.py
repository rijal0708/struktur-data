#implementasi pada python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Contoh penggunaan pada python:
nilai = Stack()
nilai.push(10) #memasukkan data pada stack
nilai.push(20)
nilai.push(30)
nilai.push(50)
print("elemen paling atas:", nilai.peek())  # mendapatkan nilai atas tampa menghapusnya
print("jumlah elemen:", nilai.size())  # melihat jumlah elemen
print("hapus elemen atas:", nilai.pop())  # menghapus elemen teratas
print("apakah stack kosong?", nilai.is_empty())  # mengecek apakah stack kosong

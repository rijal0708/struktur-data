from collections import deque  #Implementasi Queue Menggunakan collections.deque (Lebih Efisien):

queue = deque()

# Enqueue (menambahkan elemen)
queue.append("rijal")
queue.append("anto")
queue.append("alex")
queue.append("borat")
print("Queue setelah enqueue:", list(queue))  

# Dequeue (menghapus elemen pertama)
queue.popleft()
print("Queue setelah dequeue:", list(queue))  

# Melihat elemen terdepan (front)
print("Elemen depan (front):", queue[0]) 

# Memeriksa apakah queue kosong
print("Apakah queue kosong?", len(queue) == 0)  

# Ukuran queue
print("Ukuran queue:", len(queue))  
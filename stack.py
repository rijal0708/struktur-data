#contoh implementasi stack
#mencetak menggunakan print()

stack = [1, 2, 3, 4, 5, 6]
hewan = ["ayam", "sapi", "ikan"]
print(stack)

stack.append(7) #memasukkan data dengan append
print("data yang masuk :", 7)
print("data saat ini", stack)

print("data keluar :", stack.pop()) #mengambil data pada stack
print("data sekarang :", stack)


def is_empty(self):  #memeriksa apakah stack kosong
   return len(self) == 0

def peek(self):  # mendapatkan nilai atas tampa menghapusnya
   if len (self) == 0:
      return "stack is empty"
   return self[-1]
      
   
print("apakah stack kosong?", is_empty(stack)) 
print("data paling atas : ", peek(hewan))

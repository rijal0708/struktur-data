# Membuat ArrayList (List)
makanan_list = []

# Menambahkan elemen
makanan_list.append("bakso")
makanan_list.append("mie ayam")
makanan_list.append("nasgor")
makanan_list.insert(1,"burger") # menambahkan elemen pada posisi tertentu
print("daftar menu:", makanan_list)  

# Mengakses elemen berdasarkan indeks
print("Elemen pertama:", makanan_list[0])  # dimulai dari kiri
print("Elemen terakhir:", makanan_list[-1])  # dimulai dari kanan

# Menghapus elemen berdasarkan indeks
makanan_list.pop(1)  # Menghapus elemen pada indeks 1 (mie ayam)
makanan_list.remove("nasgor") #menghapus elemen dengan nilai tertentu
print("menu setelah penghapusan:", makanan_list)  

# Mengganti elemen
makanan_list[0] = "steak"
print("menu setelah penggantian:", makanan_list)  

#menghitung jumlah elemen
print("jumlah menu saat ini:", len(makanan_list))
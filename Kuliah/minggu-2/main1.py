import tkinter as tk
from tkinter import messagebox

# def hitung_luas_trapesium():
#     try:
#         # Mengambil input dari entry
#         sisi_a = float(entry_sisi_a.get())
#         sisi_b = float(entry_sisi_b.get())
#         tinggi_luas = float(entry_tinggi_luas.get())
#         # Proses
#         luas_trapesium = 0.5 * (sisi_a + sisi_b) * tinggi_luas
#         # Menampilkan Hasil
#         messagebox.showinfo("Hasil", f"Luas Trapesium Anda Adalah : {luas_trapesium}")
#     except ValueError:
#         messagebox.showinfo("Error", "Masukkan Angka Yang Valid!")

# # Membuat Jendela Utama
# root = tk.Tk()
# root.title("Kalkulator Menghitung Luas Trapesium")

# # Membuat Label dan entry untuk Sisi A
# label_sisi_a = tk.Label(root, text = "Masukkan Nilai Sisi A : ")
# label_sisi_a.pack()
# entry_sisi_a = tk.Entry(root)
# entry_sisi_a.pack()

# # Membuat Label dan entry untuk Sisi B
# label_sisi_b = tk.Label(root, text = "Masukkan Nilai Sisi B : ")
# label_sisi_b.pack()
# entry_sisi_b = tk.Entry(root)
# entry_sisi_b.pack()

# # Membuat Label dan Entry untuk Tinggi
# label_tinggi_luas = tk.Label(root, text = "Masukkan Tinggi : ")
# label_tinggi_luas.pack()
# entry_tinggi_luas = tk.Entry(root)
# entry_tinggi_luas.pack()

# # Membuat tombol untuk menghitung Luas
# button_hitung_luas = tk.Button(root, text = "Hitung Luas", command=hitung_luas_trapesium)
# button_hitung_luas.pack()

# root.mainloop()

# def hitung_keliling_trapesium():
#     try:
#         # Mengambil input dari entry
#         sisi_alas = float(entry_sisi_alas.get())
#         sisi_atas = float(entry_sisi_atas.get())
#         garis_miring = float(entry_garis_miring.get())
#         # Proses
#         keliling_trapesium = sisi_alas + sisi_atas + garis_miring + garis_miring
#         # Menampilkan Hasil
#         messagebox.showinfo("Hasil", f"Keliling Trapesium Anda Adalah : {keliling_trapesium}")
#     except ValueError:
#         messagebox.showinfo("Error", "Masukkan Angka Yang Valid!")

# # Membuat Jendela Utama
# root = tk.Tk()
# root.title("Kalkulator Menghitung Keliling Trapesium")

# # Membuat Label dan entry untuk Sisi Alas
# label_sisi_alas = tk.Label(root, text = "Masukkan Nilai Sisi Alas : ")
# label_sisi_alas.pack()
# entry_sisi_alas = tk.Entry(root)
# entry_sisi_alas.pack()

# # Membuat Label dan entry untuk Sisi Atas
# label_sisi_atas = tk.Label(root, text = "Masukkan Nilai Sisi Atas : ")
# label_sisi_atas.pack()
# entry_sisi_atas = tk.Entry(root)
# entry_sisi_atas.pack()

# # Membuat Label dan Entry untuk Garis Miring
# label_garis_miring = tk.Label(root, text = "Masukkan Garis Miring : ")
# label_garis_miring.pack()
# entry_garis_miring = tk.Entry(root)
# entry_garis_miring.pack()

# # Membuat tombol untuk menghitung garis_miring
# button_hitung_garis_miring = tk.Button(root, text = "Hitung Keliling", command=hitung_keliling_trapesium)
# button_hitung_garis_miring.pack()

# root.mainloop()

# Luas dan Keliling Trapesium

# Luas
# print('MENGHITUNG LUAS TRAPESIUM')

# sisi_a = float(input('Masukkan Nilai Sisi A : '))
# sisi_b = float(input('Masukkan Nilai Sisi B : '))
# tinggi = float(input('Masukkan Nilai Tinggi : '))

# luas = 0.5 * (sisi_a + sisi_b) * tinggi

# print(f'Luas Trapesium Anda Adalah : {luas}')

# # Keliling Trapesium
# sisi_alas = float(input('Masukkan Nilai Alas : '))
# sisi_atas = float(input('Masukkan Nilai Sisi Atas : '))
# tinggiKeliling = float(input('Masukkan Nilai Tinggi : '))
# garis_miring = float(input('Masukkan Nilai Garis Miring : '))

# keliling = sisi_alas + sisi_atas + garis_miring + garis_miring

# print(f'Keliling Trapesium Anda Adalah : {keliling}') 

# Luas dan Keliling Persegi Panjang
# def hitung_luas_persegi_panjang():
#     try:
#         # Mengambil input dari entry
#         panjang = float(entry_panjang.get())
#         lebar = float(entry_lebar.get())
#         # Proses
#         luas_persegi_panjang = panjang * lebar        # Menampilkan Hasil
#         messagebox.showinfo("Hasil", f"Luas Persegi Panjang Anda Adalah : {luas_persegi_panjang}")
#     except ValueError:
#         messagebox.showinfo("Error", "Masukkan Angka Yang Valid!")

# # Membuat Jendela Utama
# root = tk.Tk()
# root.title("Kalkulator Menghitung Luas Persegi Panjang")

# # Membuat Label dan entry untuk Sisi A
# label_panjang = tk.Label(root, text = "Masukkan Nilai Panjang : ")
# label_panjang.pack()
# entry_panjang = tk.Entry(root)
# entry_panjang.pack()

# # Membuat Label dan entry untuk Sisi B
# label_lebar = tk.Label(root, text = "Masukkan Nilai Lebar : ")
# label_lebar.pack()
# entry_lebar = tk.Entry(root)
# entry_lebar.pack()

# # Membuat tombol untuk menghitung Luas
# button_hitung_luas = tk.Button(root, text = "Hitung Luas", command=hitung_luas_persegi_panjang)
# button_hitung_luas.pack()

# root.mainloop()

def hitung_keliling_persegi_panjang():
    try:
        # Mengambil input dari entry
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        # Proses
        keliling_persegi_panjang = 2 * (panjang + lebar)        # Menampilkan Hasil
        messagebox.showinfo("Hasil", f"Keliling Persegi Panjang Anda Adalah : {keliling_persegi_panjang}")
    except ValueError:
        messagebox.showinfo("Error", "Masukkan Angka Yang Valid!")

# Membuat Jendela Utama
root = tk.Tk()
root.title("Kalkulator Menghitung Keliling Persegi Panjang")

# Membuat Label dan entry untuk Sisi A
label_panjang = tk.Label(root, text = "Masukkan Nilai Panjang : ")
label_panjang.pack()
entry_panjang = tk.Entry(root)
entry_panjang.pack()

# Membuat Label dan entry untuk Sisi B
label_lebar = tk.Label(root, text = "Masukkan Nilai Lebar : ")
label_lebar.pack()
entry_lebar = tk.Entry(root)
entry_lebar.pack()

# Membuat tombol untuk menghitung Luas
button_hitung_luas = tk.Button(root, text = "Hitung Keliling", command=hitung_keliling_persegi_panjang)
button_hitung_luas.pack()

root.mainloop()
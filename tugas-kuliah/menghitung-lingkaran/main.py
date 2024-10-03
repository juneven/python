import tkinter as tk
from tkinter import messagebox

# def hitung_luas_lingkaran():
#     try:
#         # Mengambil input dari entry
#         jari_jari = float(entry_jari_jari.get())
#         # Proses
#         luas_lingkaran = 3.14 * jari_jari * jari_jari
#         # Menampilkan Hasil
#         messagebox.showinfo("Hasil", f"Luas Lingkaran Anda Adalah : {luas_lingkaran}")
#     except ValueError:
#         messagebox.showinfo("Error", "Masukkan Angka Yang Valid!")

# # Membuat Jendela Utama
# root = tk.Tk()
# root.title("Kalkulator Menghitung Luas Lingkaran")

# # Membuat Label dan entry untuk Jari-Jari
# label_jari_jari = tk.Label(root, text = "Masukkan Nilai Jari-Jari : ")
# label_jari_jari.pack()
# entry_jari_jari = tk.Entry(root)
# entry_jari_jari.pack()

# # Membuat tombol untuk menghitung Luas
# button_hitung_luas = tk.Button(root, text = "Hitung Luas", command=hitung_luas_lingkaran)
# button_hitung_luas.pack()

# root.mainloop()

def hitung_keliling_lingkaran():
    try:
        # Mengambil input dari entry
        diameter = float(entry_diameter_lingkaran.get())
        # Proses
        keliling_lingkaran = 22/7 * diameter
        # Menampilkan Hasil
        messagebox.showinfo("Hasil", f"Keliling Lingkaran Anda Adalah : {keliling_lingkaran}")
    except ValueError:
        messagebox.showinfo("Error", "Masukkan Angka Yang Valid!")

# Membuat Jendela Utama
root = tk.Tk()
root.title("Kalkulator Menghitung Keliling Lingkaran")

# Membuat Label dan entry untuk Diameter
label_diameter_lingkaran = tk.Label(root, text = "Masukkan Nilai Diameter : ")
label_diameter_lingkaran.pack()
entry_diameter_lingkaran = tk.Entry(root)
entry_diameter_lingkaran.pack()

# Membuat tombol untuk menghitung Luas
button_hitung_luas = tk.Button(root, text = "Hitung Keliling", command=hitung_keliling_lingkaran)
button_hitung_luas.pack()

root.mainloop()
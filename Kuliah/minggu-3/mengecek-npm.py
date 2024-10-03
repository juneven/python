import tkinter as tk
from tkinter import messagebox

# Latihan No. 1

# npm = input('Masukkan NPM Anda : ')

# def mengecekNPM(npm):
#     if npm == '130029':
#         return 'Dinda'
#     elif npm == '130102':
#         return 'Rino'
#     else:
#         return 'NPM Anda Tidak Terdaftar'

# nama_mahasiswa = mengecekNPM(npm)

# print(f'{nama_mahasiswa}')

def mengecek_npm():
    try:
        npm = int(entry.get())
        if npm == 130029:
            nama_mahasiswa = "Dinda"
        elif npm == 130102:
            nama_mahasiswa = "Rino"
        else:
            nama_mahasiswa = "NPM Anda Tidak Terdaftar di Sistem"
        
        messagebox.showinfo("Pengecekan NPM", f"NPM: {npm}\nNama: {nama_mahasiswa}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Silahkan masukkan NPM yang valid.")
        
# Create the main window
root = tk.Tk()
root.title("Pengecekan NPM")

# Create and place the Label and entry for input
label = tk.Label(root, text="Masukkan NPM Mahasiswa:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

# Create and place the button to check the NPM
button = tk.Button(root, text="Cek", command=mengecek_npm)
button.pack(pady=20)

# Run the application
root.mainloop()
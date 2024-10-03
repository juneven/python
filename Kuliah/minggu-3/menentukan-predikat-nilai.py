import tkinter as tk
from tkinter import messagebox

# nilai = int(input('Masukkan Nilai Anda : '))

# if nilai >= 86 and nilai <= 100:
#     print('Nilai Anda Sangat Baik')
# elif nilai <= 85 and nilai >= 76:
#     print('Nilai Anda Baik')
# elif nilai <= 75 and nilai >= 66:
#     print('Nilai Anda Cukup')
# elif nilai <= 65 and nilai >= 56:
#     print('Nilai Anda Kurang')
# elif nilai > 100:
#     print('Anda Memasukkan Nilai Lebih Dari 100')
# else:
#     print('Anda Gagal')

def evaluate_score():
    try:
        nilai = int(entry.get())
        if nilai >= 86 and nilai <= 100:
            result = "Sangat Baik"
        elif nilai >= 76 and nilai < 85:
            result = "Baik"
        elif nilai >= 66 and nilai < 75:
            result = "Cukup"
        elif nilai >= 56 and nilai < 65:
            result = "Kurang"
        elif nilai <= 55:
            result = "Gagal"
        elif nilai > 100:
            result = "Angka yang anda masukkan tidak valid"
        else:
            result = "Maaf, format nilai tidak sesuai"
    
        messagebox.showinfo("Hasil Evaluasi", f"Nilai: {nilai}\nPredikat: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Silahkan masukkan nilai yang valid.")
        
# Create the main window
root = tk.Tk()
root.title("Evaluasi Nilai Siswa")

# Create and place the Label and entry for input
label = tk.Label(root, text="Masukkan Nilai Siswa:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

# Create and place the button to evaluate the score
button = tk.Button(root, text="Evaluasi", command=evaluate_score)
button.pack(pady=20)

# Run the application
root.mainloop()
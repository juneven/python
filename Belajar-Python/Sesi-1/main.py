import random

welcome_message = 'WELCOME TO CUYPY GAMES'

cuypy_position = random.randint(1, 4)

print('********************************************')
print(f'********* {welcome_message} ***********')
print('********************************************')

nama_user = input('Silakan Masukkan Nama Kamu : ')

print(f'''
Selamat Datang {nama_user} di CUYPY GAMES!!!

OKE! {nama_user}, Tolong Perhatikan Goa Dibawah Ini!!

|_| |_| |_| |_|
''')

pilihan_user = int(input('Menurut Kamu CUYPY Berada Goa Yang Mana? [1] / [2] / [3] / [4] : '))

konfirmasi_user = input(f'Apakah Kamu Sudah Yakin Dengan Pilihan Goa Kamu Yaitu Goa {pilihan_user} : [y/n] : ')

if konfirmasi_user == 'y':
    print(f'Pilihan Goa Kamu Adalah Goa {pilihan_user}')

    if pilihan_user == cuypy_position:
        print(f'Selamat {nama_user}, Kamu Menebak Benar Posisi CUYPY ada di Goa {cuypy_position} dan Pilihan Kamu adalah Goa {pilihan_user}')
    else:
        print(f'Sayang Sekali {nama_user}, Tebakan Kamu Salah, Posisi CUYPY ada di Goa {cuypy_position} dan pilihan kamu adalah Goa {pilihan_user}')    
elif konfirmasi_user == 'n':
    print('Silakan Ulang Jalankan Programnya...')
else:
    print('Kamu Tidak Memilih Yes dan No')
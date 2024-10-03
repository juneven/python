total_belanja = int(input('Masukkan Total Belanja Anda : '))

if total_belanja > 300000 :
    total_bayar = total_belanja  * 15 / 100
    
    print(total_bayar)
else: 
    print(total_belanja)
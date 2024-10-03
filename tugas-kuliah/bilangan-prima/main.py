def menentukanBilanganPrima(angka):
    pembagi = 0
    
    if angka == 1:
        return f'{angka} bukan Bilangan Prima'
    else:
        i = 1
        
        while i <= angka:
            if angka % i == 0:
                pembagi += 1
            i += 1
    
    if pembagi == 2:
        print(f'{angka} adalah Bilangan Prima')
    else:
        print(f'{angka} bukan Bilangan Prima')


menentukanBilanganPrima(2) 
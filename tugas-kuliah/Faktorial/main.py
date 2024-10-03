def faktorial(angka):  
    if angka == 0:
        return 1

    return angka * faktorial(angka - 1)
    

print(faktorial(5))
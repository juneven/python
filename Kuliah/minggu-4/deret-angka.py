i = 1

while i < 40 :
    print(i, end='')
    
    i += 1

    j = i
    
    while j <= i :
        if j == 40 :
            break
        
        print(end='+')
        
        j += 1
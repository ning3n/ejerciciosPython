for i in range(1, 101):
    if i>1:
        count = 0
        j = 2
        while j<i and count==0:
            prueba=i%j
            if prueba ==0:
                count=count+1
            j = j + 1
        
        if count==0:
            print(i, end=", ")
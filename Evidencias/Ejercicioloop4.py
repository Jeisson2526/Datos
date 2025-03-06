def Sumaacom():
    n=1
    c=0
    sum=0
    while n!=0:
        if n<0:
            break
        else:
            n=int(input("Introduzca el numero:  "))
            if n<0:
                break
            else:
                sum=sum+n
                c=c+1
                print("La suma es: ",sum)
    return c-1
    
print(Sumaacom())
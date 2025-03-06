def opuesto():
    n=1
    c=0
    sum=0
    while n!=0:
        n=int(input("Ingrese numero"))
        sum=sum+n
        c=c+1
    pro=sum/(c-1)
    return pro
print("El promedio es:  ",opuesto())

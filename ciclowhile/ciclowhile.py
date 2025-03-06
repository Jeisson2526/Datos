def opuesto():
    n=1
    c=0
    while n!=0:
        n=int(input("Ingrese numero"))
        print(n*-1)
        c=c+1
    return c-1

print(opuesto())
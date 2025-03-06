def media(lista):
    suma = 0
    n = 0
    for numero in lista:
        suma += numero
        n += 1
    return suma / n

def mitades(lista):
    tam=len(lista)
    print(tam)
    if tam%2!=0:
        m=media(lista)
        lista.append(int(m))
        tam=len(lista)
        print(lista)
    r1=lista[:int(lista)/2]
    r2=lista[int(lista)/2:]
    print(f"Mitad1= {r1}")
    print(f"Mitad2= {r2}")
    return r1,r2
print(mitades)
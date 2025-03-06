def llenarlista(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=int(input("Ingrese numero"))
        lista.append(num)
    return lista
vector=[]
print(llenarlista(vector,5))
print(vector)
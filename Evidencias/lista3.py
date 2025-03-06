lista=[]

for i in range(11):
    lista.append(i*10)
print(lista)
def llenarlista(lista,cantidad):
    lista=[]
    for i in range(cantidad):
        lista.append(i*10)
    return lista
print(llenarlista(lista,5))
#print("-"*20)
#llenarlista(10)
#print("-"*20)
#llenarlista(15)
#print("-"*20)
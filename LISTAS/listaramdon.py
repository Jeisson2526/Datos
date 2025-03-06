import random
def llenarlistaRandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

vec=[]
tan=int(input("Cuantos numeros ingreso a la lista"))
vec=llenarlistaRandom(vec,tan)
print(vec)
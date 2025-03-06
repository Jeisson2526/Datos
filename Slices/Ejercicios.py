import random
def rebanadas(lista, ini, fin):
    if ini > len(lista) or fin < len(lista)*-1:
        return ("Fuera del rango de la lista")
    else:
        return lista[ini:fin]



def llenarlistaRandom(lista):
    lista=[]
    cantidad=random.randint(5,20)
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

vec=[]
vec=llenarlistaRandom(vec)
print(vec)
reb1=rebanadas(vec,5,9)
print(reb1)
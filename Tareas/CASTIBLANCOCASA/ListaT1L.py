import random

def llenarlistaRandom(cantidad):
    lista = []
    for i in range(cantidad):
        num = random.randint(1, 100)
        lista.append(num)
    return lista

def sumar_lista(lista):
    return sum(lista)

tan = random.randint(5,20 )
if tan >4 and tan < 21:
    vec = llenarlistaRandom(tan)
    print("La lista generada es:", vec)
    resultado_suma = sumar_lista(vec)
    print("La suma de los elementos de la lista es:", resultado_suma)
else:
    print("Error intente nuevamente")  
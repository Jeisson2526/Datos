import random
def llenarlistaRandom(lista,cantidad):
    for i in range(cantidad):
        num = random.randint(1, 100)
        lista.append(num)
    return lista

def calcular_promedio(lista):
    if len(lista) == 0:
        return 0  
    return sum(lista) / len(lista)
lista = []
can=random.randint(5,20)
lista = llenarlistaRandom(lista,can)
resultado_promedio = calcular_promedio(lista)
print(lista)
print("El promedio de los elementos de la lista es:", resultado_promedio)

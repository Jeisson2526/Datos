import random

def lista(n, minimo=1, maximo=100):
    return[random.randint(minimo, maximo)for_in range(n)]

def frecuencia_Absoluta():
    frecuencia=[]
    for elemento in lista:
        frecuencia[elemento]=frecuencia
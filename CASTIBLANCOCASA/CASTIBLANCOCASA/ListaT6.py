import math 
lista = [10, 20, 30, 40, 50]
def calcular_media(lista):
    suma = 0
    n = 0
    for numero in lista:
        suma += numero
        n += 1
    return suma / n
def calcular_varianza(lista):
    media = calcular_media(lista)  
    suma_cuadrados = 0
    n = 0
    for numero in lista:
        suma_cuadrados += (numero - media) ** 2  
        n += 1
    return suma_cuadrados / n  

def calcular_desviacion_estandar(lista):
    varianza = calcular_varianza(lista)  
    return math.sqrt(varianza)  

print("La lista es:", lista)
print("La desviación estándar de la lista es:", calcular_desviacion_estandar(lista))
lista = [10,20,30,40,50]
def calcular_media(lista):
    suma = 0
    n = 0
    for numero in lista:
        suma += numero
        n += 1
    return suma / n
#----------------------------------------------------------------
def calcular_varianza(lista):
    media = calcular_media(lista)  
    suma_cuadrados = 0
    n = 0
    for numero in lista:
        suma_cuadrados += (numero - media) ** 2  
        n += 1
    return suma_cuadrados / n  

print("La lista es:", lista)
print("La varianza de la lista es:", calcular_varianza(lista))
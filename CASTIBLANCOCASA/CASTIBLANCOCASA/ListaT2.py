def calcular_promedio(lista):
    if len(lista) == 0:
        return 0  
    return sum(lista) / len(lista)

lista = [10, 20, 30, 40, 50]
resultado_promedio = calcular_promedio(lista)
print("El promedio de los elementos de la lista es:", resultado_promedio)
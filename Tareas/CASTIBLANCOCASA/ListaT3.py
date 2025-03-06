lista = [10, 20, 30, 40, 50]
def hallar_mayor(lista):
    return max(lista) if len(lista) > 0 else "La lista está vacía, no hay mayor elemento."

print("La lista es:", lista)
print("El mayor elemento de la lista es:", hallar_mayor(lista))
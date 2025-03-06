import random
def llenarlistaRandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

vec=[]
tan1=int(input("Cuantos numeros ingreso a la lista"))
vec=llenarlistaRandom(vec,tan1)
print(vec)
#--------------------------------------------
def sumar_lista(vec):
    return sum(vec)
resultado_suma = sumar_lista(vec)
#---------------------------------------------------------------
def calcular_promedio(vec):
    if len(vec) == 0:
        return 0  
    return sum(vec) / len(vec)
resultado_promedio = calcular_promedio(vec)
#----------------------------------------------------------------
def hallar_mayor(vec):
    return max(vec) if len(vec) > 0 else "La lista está vacía, no hay mayor elemento."

#----------------------------------------------------------------
def hallar_menor(vec):
    return min(vec)  

#------------------------------------------------------------------
def OrdeAsc(vec):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(vec) - 1):
            if vec[i] > vec[i + 1]:
                swapped = True 
                vec[i], vec[i + 1] = vec[i + 1], vec[i]
    return vec

#--------------------------------------------------------------------

swapped = True
def OrdeDes(vec):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(vec) - 1):
            if vec[i] < vec[i + 1]:
                swapped = True 
                vec[i], vec[i + 1] = vec[i + 1], vec[i]
    return vec

#---------------------------------------------------------------
#moda camilo en espera 

#---------------------------------------------------------------
def calcular_media(vec):
    suma = 0
    n = 0
    for numero in vec:
        suma += numero
        n += 1
    return suma / n
def calcular_varianza(vec):
    media = calcular_media(vec)  
    suma_cuadrados = 0
    n = 0
    for numero in vec:
        suma_cuadrados += (numero - media) ** 2  
        n += 1
    return suma_cuadrados / n  

print("1-sumar")
print("2-promedio")
print("3-hallar_mayor")
print("4-hallar_menor")
print("5-hallar_asendente")
print("6-hallar_desendente")
print("7-hallar varianza")

sel=int(input("Seleccione opcion"))

match sel:
    case 1:
        def sumar_lista(vec):
            return sum(vec)
        resultado_suma = sumar_lista(vec)
        print("La suma de los elementos de la lista es:", resultado_suma)

    case 2:
        def calcular_promedio(vec):
            if len(vec) == 0:
                return 0  
            return sum(vec) / len(vec)
        resultado_promedio = calcular_promedio(vec)
        print("El promedio de los elementos de la lista es:", resultado_promedio)
        
    case 3:
        def hallar_mayor(vec):
            return max(vec) if len(vec) > 0 else "La lista está vacía, no hay mayor elemento."

        print("El mayor elemento de la lista es:", hallar_mayor(vec))
        
    case 4:
        def hallar_menor(vec):
            return min(vec)  

        print("El menor elemento de la lista es:", hallar_menor(vec))
        
    case 5:
        def OrdeAsc(vec):
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(vec) - 1):
                    if vec[i] > vec[i + 1]:
                        swapped = True 
                        vec[i], vec[i + 1] = vec[i + 1], vec[i]
            return vec
        print("El orden ascendente es :", OrdeAsc(vec))
        
    case 6:
        swapped = True
        def OrdeDes(vec):
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(vec) - 1):
                    if vec[i] < vec[i + 1]:
                        swapped = True 
                        vec[i], vec[i + 1] = vec[i + 1], vec[i]
            return vec
        print("El orden descendente es :", OrdeDes(vec))
        
    case 7:
        def calcular_media(vec):
            suma = 0
            n = 0
            for numero in vec:
                suma += numero
                n += 1
            return suma / n
        def calcular_varianza(vec):
            media = calcular_media(vec)  
            suma_cuadrados = 0
            n = 0
            for numero in vec:
                suma_cuadrados += (numero - media) ** 2  
                n += 1
            return suma_cuadrados / n  
        print("La varianza de la lista es:", calcular_varianza(vec))
        
    case 8:
        def
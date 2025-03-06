import random
listas = [20 for i in range(5)]
print(listas)
lista = [i*i for i in range(1,6)]
print(lista)
tam=(random.randint(5,10))
lista=[random.randint(0,100) for i in range(tam)]
print(lista)

lista2 = [i for i in lista]
print(f"lista2={lista2}")#variables constantes operadores estructuras(expresion, elemento y conjuntos)


lista3 = [0 if x%2==0 else x for x in lista]
print(f"lista3={lista3}")

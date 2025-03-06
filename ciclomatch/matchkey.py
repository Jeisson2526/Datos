#Condicionales

#if else, match -case, for, while
x=5
if x%2==0:
    print("El numero es par")
else:
    print("El numero es impar")
    
    
# Dos numeros ascendente o descendente
a =(input("Escriba el primer digito: "))
b =(input("Escriba el segundo digito: "))

if a > b:
    print(a," es mayor que",b)
elif a < b:
    print(a,"es menor que",b)
else:
    print("Los numeros son iguales")
    
    
Est=(int(input("Digite el numero de su estrato:  ")))
match Est:
    case 1:
        print("Estrato 1")
    case 2:
        print("Estrato 2")
    case 3:
        print("Estrato 3")
    case 4:
        print("Estrato 4")
    case 5:
        print("Estrato 5")
    case 6:
        print("Estrato 6")
    case _:
        print("Estrato no valido")
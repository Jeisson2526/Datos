def valor_del_medio(num1,num2,num3):
    numeros = [num1, num2, num3]
    numeros.sort
    return numeros[1]
num1 = int(input("Introduce el primer numero"))
num2 = int(input("Introduce el segundo numero"))
num3 = int(input("Introduce el tercer numero"))
resultado = valor_del_medio(num1,num2,num3)
print("El valor del medio es:", resultado)
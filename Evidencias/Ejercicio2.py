def comparar_numeros(num1,num2,num3):
    if num1 == num2 == num3:
        return "Los tres numeros son iguales."
    elif num1 == num2 or num1 == num3 or num2 == num3:
        return "Hay dos numeros iguales."
    else:
        return"Los tresnumeros son distintos"
num1 =int(input("Primer numero: "))
num2 = int(input("Sengundo numero: "))
num3 = int(input("Tercer numero") )
resultado = comparar_numeros(num1,num2,num3)
print (resultado)
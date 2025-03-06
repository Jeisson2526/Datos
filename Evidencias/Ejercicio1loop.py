def intervenir_numero(numero):
    return numero[::-1]
numero = input("Un numero de hasta 9digitos: ")
numero_invertido = intervenir_numero(numero)
print("Numeroinvertido:", numero_invertido)
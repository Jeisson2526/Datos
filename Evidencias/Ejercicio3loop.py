def es_numero_perfecto(n):
    if n <= 1:
        return False
    suma_divisores = 0
    
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
            return suma_divisores == n
        numero = int(input("Ingresa un numero para verificar si esperfecto: "))
        if es_numero_perfecto(numero):
            print(f"{numero} es un numero perfecto.")
        else:
            print(f"{numero} no es un numero perfecto.")
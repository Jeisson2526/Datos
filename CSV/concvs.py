import csv

# Función para leer el archivo CSV y encontrar el salario más alto y más bajo
def obtener_salarios():
    salarios = []
    try:
        with open('datos.csv', mode='r', newline='') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Convertir el salario a float (ignorando valores vacíos o no válidos)
                    salario = float(fila['SALARY'])
                    salarios.append(salario)
                except ValueError:
                    print(f"Valor no válido en la columna 'SALARY' en la fila: {fila}")
        if salarios:
            salario_maximo = max(salarios)
            salario_minimo = min(salarios)
            return salario_maximo, salario_minimo
        else:
            return None, None
    except FileNotFoundError:
        print("El archivo 'datos.csv' no se encuentra.")
        return None, None

# Obtener y mostrar los salarios
salario_max, salario_min = obtener_salarios()
if salario_max is not None and salario_min is not None:
    print(f"Salario más alto: {salario_max}")
    print(f"Salario más bajo: {salario_min}")
else:
    print("No se pudieron obtener los salarios.")
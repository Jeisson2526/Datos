def notas():
        nota = float(input("Introduce una nota entre 0 y 10: "))
        if nota < 0 or nota > 10:
            print("La nota está fuera del rango permitido")
            return 
        if 0 <= nota < 5:
            print("Insuficiente")
        elif 5 <= nota < 6:
            print("Suficiente")
        elif 6 <= nota < 7:
            print("Bien")
        elif 7 <= nota < 9:
            print("Notable")
        else:
            print("Sobresaliente")
notas()
def buscarpalabra():
    palabra = input("Ingresa la palabra que deseas buscar: ")
    with open("archivos/himnoF.txt", 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().lower()
            palabras = contenido.split()
            cantidad = 0
            for i in palabras:
                if i == palabra:
                    cantidad += 1
            if cantidad > 0:
                print("La palabra seleccionada si se encuentra y aparece la siguiente cantidad de veces",cantidad )
            else:
                print("La palabra no aparece en el archivo")

buscarpalabra()

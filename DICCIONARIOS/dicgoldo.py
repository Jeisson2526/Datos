datos = {    "gender": "female",
    "date_of_birth": "05.08.02",
    "enrollment_semester": "Summer 2022",
    "semester_number": 6,
    "major": "Data Analytics",
    "number": 22100
    
}
def nuevaclave(dict, clave, valor):
    flag = False
    for key in dict.keys():
        if key == clave:
            return("La clave ya existe")
        else:
            flag = True
    if flag == True:
        dict[clave]=valor
        

miclave = input("Ingrese una clave :")
mivalor = input("Ingrese el valor :")
nuevaclave(datos,miclave,mivalor)
print(datos)
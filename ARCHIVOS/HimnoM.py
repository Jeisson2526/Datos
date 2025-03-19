with open ("archivos/himnoF.txt") as pointer:
    st = pointer.read()
    contma = 0
    contmi = 0
    for letra in st:
        if letra.isupper()==True:
            contma += 1
        elif letra.islower()==True:
            contmi += 1
            
print(contma)
print(contmi)
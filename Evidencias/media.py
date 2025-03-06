def media():
    can=int(input("Digite cuantos numeros"))
    sum=0
    for i in range(1,can+1,1):
        tn=int(input("ingrese un numero"))
        sum+=tn
        m=sum/can
    print("la media es",m)
    return m
media()
 
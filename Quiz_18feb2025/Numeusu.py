def imprimir_serie():
        D1=int(input("Digite el primer numero"))
        D2=int(input("Digite el segundo numero"))
        if D1<D2:
            for i in range(D1,D2+1,):
                print(i)
        else:
            if D1>D2:
                for i in range(D1,D2-1,-1):
                    print(i)
imprimir_serie()
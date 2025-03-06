def series():
    D1=int(input("Digite el primer numero"))
    D2=int(input("Digite el segundo numero"))
    if D1<D2:
        for i in range(D1,D2+1,1):
            if i%7==0:
                print(i)
        else:
            if D1>D2:
                for i in range(D1,D2-1,-1):
                    if i%7==0:
                        print(i)

series()
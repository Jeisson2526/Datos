import random
def llenarListaRandom(lista,cantidad):
    lista=[]
    num=0
    
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista
tam=random.randint(10,50)
vec=[]
vec=llenarListaRandom(vec,tam)
print("Lista original, ",vec)
print("su longitud es :",len(vec))
print("\n")


def CalFrecue(vec):
    LisFrec = []
    Con = []

    for num in vec:
        if num not in Con:
            frecuencia = 0
            for i in vec:
                if i == num:
                    frecuencia += 1
            LisFrec.append(frecuencia)
            Con.append(num)

    return LisFrec

def SumList(vec):
    total=0
    for i in vec:
        total+=i
    return total


def FreRel(FreVec):
    Fr=[]
    Res=0
    for i in FreVec:
        Res=i/SumFre
        Fr.append(Res)
        
    return Fr


def Porcentaje(FreRela):
    Porc=[]
    Res=0
    for i in FreRela:
        Res=i*100
        Porc.append(Res)
    return Porc

FreVec=CalFrecue(vec) 
FreRela=FreRel(FreVec)
        
def FreAbsoAcom(FreVec):
    FreA=[]
    F=0
    for i in FreVec:
        F=F+i
        FreA.append(F)      
    return FreA
    





SumFre=SumList(FreVec) 
Porc=Porcentaje(FreRela)
FreAbsAcomu=FreAbsoAcom(FreVec)


print("La frecuencia es:",FreVec)
print("La suma de la frecuencia es :",SumFre)
print("-"*150)


print("la Frecuencia relativa es :",FreRela)

print("\n")
print("-"*150)

print("El porcentaje es:  ",Porc)
print("\n")
print("-"*150)

print("La frecuencia abosluta acomulada es :  ",FreAbsAcomu)
print("\n")
print("-"*150)
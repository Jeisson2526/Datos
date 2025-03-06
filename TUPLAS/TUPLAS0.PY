import random
tupla = 10,
tupla= tupla + (20,)
print(type(tupla))
print(tupla[0])
tupla2=(1,)
cantidad=random.randint(5,10)
for i in range(cantidad):
    num = random.randint(1,100)
    tupla2 += (num,)
print(tupla2)
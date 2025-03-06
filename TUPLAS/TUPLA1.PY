import random
tupla = 10,
tupla= tupla + (20,)
print(type(tupla))
print(tupla[0])
num = random.randint(1,100)
tupla2=(num,)
cantidad=random.randint(5,10)
for i in range(cantidad):
    num = random.randint(1,100)
    tupla2 += (num,)

print(tupla2)

print(f"count = {tupla.count(36)}")
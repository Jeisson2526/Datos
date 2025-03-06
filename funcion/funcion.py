def funcion(num1, num2):
    return num1 * num2

print(funcion(2,5))
print(funcion(5,2))
#------------------------------------------------------
def funcion(num1, num2):
    return num1 * num2

print(funcion(2,5))
print(funcion(num2=5,num1=2))
print(funcion(10))
#------------------------------------------------------
def funcion(num1, num2=2):
    return num1 * num2

print(funcion(2,5))
print(funcion(num2=5,num1=2))
print(funcion(10))
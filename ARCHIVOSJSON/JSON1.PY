import json

with open("ARCHIVOSJSON/EMPLOYS.JSON","r",encoding="utf-8") as eljeison:
    data=json.load(eljeison)
    sal = []
    for element in data:
        sal.append(int(element["SALARY"]))
        print(element["SALARY"])
        print("-" * 20)
print(sal)
#----------------------------------------------------------------------------
emple=[]

for i in data:
    if i['DEPARTMENT_ID']=='50':
        emple.append(i)

for i in emple:
    print(i['FIRST_NAME'],i['LAST_NAME'])
#-----------------------------------------------------------------------------
def calcular_promedio(sal):
    if len(sal) == 0:
        return 0  
    return sum(sal) / len(sal)

resultado_promedio = calcular_promedio(sal)
print("El promedio de los elementos de la lista es:", resultado_promedio)
#----------------------------------------------------------------------------
newdata ={}



#codigo que haga el promedio del salario y meter en una lista los empleados el departamento que pertenece el id 50

newdata =[
    {
        "EMPLOYEE_ID": "200",
        "FIRST_NAME": "Donald",
        "LAST_NAME": "OConnell",
        "EMAIL": "DOCONNEL",
        "PHONE_NUMBER": "650.507.9833",
        "HIRE_DATE": "21-JUN-07",
        "JOB_ID": "SH_CLERK",
        "SALARY": "4000",
        "COMMISSION_PCT": " - ",
        "MANAGER_ID": "15",
        "DEPARTMENT_ID": "50"
    }
]
data.append(newdata)
with open ("ARCHIVOSJSON/EMPLOYS.JSON","w",encoding="utf-8") as eljeison:
    json.dump(data,eljeison)
#--------------------------------------------------------------------------
newdata =[
    {
        "EMPLOYEE_ID": input("Digite el ID del empleado"),
        "FIRST_NAME": input("Digite el nombre del empleado"),
        "LAST_NAME": input("Digite el apellido del empleado"),
        "EMAIL": input("Digite el Email del empleado"),
        "PHONE_NUMBER": input("Digite el numero de telefono del empleado"),
        "HIRE_DATE": input("Digite la fecha de contratacion del empleado"),
        "JOB_ID": input("Digite el ID de trabajo del empleado"),
        "SALARY": "2000",
        "COMMISSION_PCT": " - ",
        "MANAGER_ID": input("Digite el ID del jefe"),
        "DEPARTMENT_ID": input("Digite ID de departamento del empleado")
    }
]
data.append(newdata)
with open ("ARCHIVOSJSON/EMPLOYS.JSON","w",encoding="utf-8") as eljeison:
    json.dump(data,eljeison)
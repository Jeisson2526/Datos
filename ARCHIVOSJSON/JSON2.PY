import json
with open("ARCHIVOSJSON/EMPLOYS.JSON","r",encoding="utf-8") as eljeison:
    data=json.load(eljeison)
    

#--------------------------------------------------------------------------
newdata =[
    {
        "EMPLOYEE_ID": input("Digite el ID del empleado :"),
        "FIRST_NAME": input("Digite el nombre del empleado :"),
        "LAST_NAME": input("Digite el apellido del empleado :"),
        "EMAIL": input("Digite el Email del empleado :"),
        "PHONE_NUMBER": input("Digite el numero de telefono del empleado :"),
        "HIRE_DATE": input("Digite la fecha de contratacion del empleado :"),
        "JOB_ID": input("Digite el ID de trabajo del empleado :"),
        "SALARY": "2000",
        "COMMISSION_PCT": " - ",
        "MANAGER_ID": input("Digite el ID del jefe :"),
        "DEPARTMENT_ID": input("Digite ID de departamento del empleado :")
    }
]
data.append(newdata)
with open ("ARCHIVOSJSON/EMPLOYS.JSON","w",encoding="utf-8") as eljeison:
    json.dump(data,eljeison)
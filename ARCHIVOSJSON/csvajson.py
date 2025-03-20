import csv
import json
with open ("ARCHIVOSJSON/EMPLOYS.CSV","r",newline="",encoding="utf-8")as elcsv:
    readercsv = csv.DictReader(elcsv)
    datacsv=[fila for fila in readercsv]
print(readercsv)
print(datacsv)

with open ("ARCHIVOSJSON/clientes.json","w",encoding="utf-8") as eljson:
    json.dump(datacsv,eljson,indent=4)
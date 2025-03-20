import json
import csv
with open("ARCHIVOSJSON/EMPLOYS.JSON","r",encoding="utf-8") as eljson:
    data = json.load(eljson)
headers = data[0].keys()
#print(headers)
#print(type(data))

with open ("ARCHIVOSJSON/EMPLOYS.csv","w") as elcsv:
    writer = csv.DictWriter(elcsv,headers)
    writer.writeheader()
    writer.writerows(data)
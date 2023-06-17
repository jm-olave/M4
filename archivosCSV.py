import csv

with open("MOCK_DATA.csv","r") as documento:
     lectura = csv.reader(documento)
     for linea in lectura:
          print(linea)

data = [
     ['nombre', 'edad', 'ciudad'],
     ['Carlos', '20', 'Santiago'],
     ['Sara', '20','Santiago'],
     ['John', '20','Santiago']
]


with open("test.csv", "w") as documento:
    escritura = csv.writer(documento)
    escritura.writerows(data)

import json
import csv

# Arreglo para almacenar los datos del archivo
data = []

# Obtenemos cada una de las lineas del archivo
f = open("D:/Labsin/labsin-pasantias-2021/1_acceso/passivedns.log", "r")
line = f.readline()
# Leemos cada una de las lineas como JSON
while(line != ''):
    if(line[0] != '{'):
        # Limpieza de los datos
        line = line.strip('\x00')
    newLine = json.loads(line)
    data.append(newLine)
    line = f.readline()

domains_file = open('1_acceso/domains.csv','w')

csv_writer = csv.writer(domains_file)

counter = 0

for domain in data:
    # Si es la primer fila, escribir los nombres de las columnas
    if(counter == 0):
        header = domain.keys()
        csv_writer.writerow(header)
        counter += 1
    
    csv_writer.writerow(domain.values())

domains_file.close()

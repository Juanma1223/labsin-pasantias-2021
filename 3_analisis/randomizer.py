# Choose random domains from file

import csv
from random import randint

f = open('D:/Labsin/labsin-pasantias-2021/3_analisis/argencon_sample.csv','a+')
writer = csv.writer(f)

with open('D:/Labsin/labsin-pasantias-2021/2_analisis_lexico/argencon.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    lines = csvfile.readlines()
    tam = len(lines)
    # DGA domains counter
    i = 0
    dgas = []
    # Normal domains counter
    j = 0
    normals = []
    while (i <= 10000 or j <= 10000):
        rand = randint(0,tam-1)
        randRow = lines[rand]
        if(randRow == '\r\n'):
            continue
        randRowLabel = randRow.split(",")[1]
        # Check if it's DGA
        if(randRowLabel.startswith('dga') and len(dgas) <= 10000):
            i +=1
            dgas.append(randRow)
        elif(len(normals) <= 10000):
            j += 1
            normals.append(randRow)        
    for row in dgas:
        # Parse row
        newRow = row.split("\n")[0]
        writer.writerow(newRow.split(","))
    for row in normals:
        newRow = row.split("\n")[0]
        writer.writerow(newRow.split(","))
f.close()
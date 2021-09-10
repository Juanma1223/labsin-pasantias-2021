import csv

f = open('D:/Labsin/labsin-pasantias-2021/2_analisis_lexico/argencon.csv','a+')
writer = csv.writer(f)

with open('D:/Labsin/labsin-pasantias-2021/2_analisis_lexico/domains.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # Representamos el id de cada fila
    id = 4429599
    for row in reader:
        # Construimos la nueva fila para insertar
        data = [row['query'],'normal','ns58',id]
        writer.writerow(data)
        id += 1

f.close()
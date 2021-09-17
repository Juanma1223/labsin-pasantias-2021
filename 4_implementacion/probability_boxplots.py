import csv
import matplotlib.pyplot as plt

normals = []
dgas = []

with open('D:/Labsin/labsin-pasantias-2021/4_implementacion/argencon_sample_myalgo_domains_predictions.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        if(row['label'].startswith('dga')):
            dgas.append(float(row['probability']))

        if(row['label'].startswith('normal')):
            normals.append(float(row['probability']))
        

plt.boxplot(normals)
plt.title("Gráfico de cajas de la probabilidad de acierto en dominios normales")
plt.show()

plt.boxplot(dgas)
plt.title("Gráfico de cajas de la probabilidad de acierto en dominios DGA")
plt.show()
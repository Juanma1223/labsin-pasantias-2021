import csv
import matplotlib.pyplot as plt

normals = 0
dga = 0
normal_labels = 0
dga_labels = 0
# Calculating domains length
normals_length = [0 for _ in range(0,250)]
dgas_length = [0 for _ in range(0,50)]

with open('D:/Labsin/labsin-pasantias-2021/3_analisis/argencon_sample_domains_predictions.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        if(row['label'].startswith('dga')):
            dga += 1
            # Saving domain's length
            dgas_length[len(row['domain'])] += 1
            # Counting correctly classified dga domains
            if(row['label_pred'].startswith('dga')):
                dga_labels += 1

        if(row['label'].startswith('normal')):
            normals += 1
            # Saving domain's length
            normals_length[len(row['domain'])] += 1
            # Counting correctly classified normal domains
            if(row['label_pred'].startswith('normal')):
                normal_labels += 1
        

print('Sensitivity:',dga_labels/dga)
print('Specificity:',normal_labels/normals)
print("Normals length:",normals_length)
print("")
print("DGA length",dgas_length)

labels = [i for i in range(0,len(normals_length))]
# Build Labels for chart bars
plt.bar(labels,normals_length)
plt.title('Normals domains length')
plt.xlabel("Domain's length")
plt.ylabel("Quantity of domains with a certain length")
plt.show()

labels = [i for i in range(0,len(dgas_length))]
# Build Labels for chart bars
plt.bar(labels,dgas_length)
plt.title('DGA domains length')
plt.xlabel("Domain's length")
plt.ylabel("Quantity of domains with a certain length")
plt.show()
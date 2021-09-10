import csv
import matplotlib.pyplot as plt

initial_character = ord("#")
last_character = ord("{")
counter = [0 for _ in range(0,last_character-initial_character)]

def count(s):
    global counter,initial_character
    for l in s:
        counter[ord(l)-initial_character] += 1

# Count characters from each domain
with open('D:/Labsin/labsin-pasantias-2021/2_analisis_lexico/argencon.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        count(row['source'])

# Rescale the counters
max = max(counter)
for i in range(0,len(counter)):
    counter[i] = counter[i]/max
labels = []
# Build Labels for chart bars
for i in range(0,len(counter)):
    labels.append(chr(i+initial_character))
lab_pos = [i for i, _ in enumerate(labels)]
plt.bar(lab_pos,counter)
plt.xlabel("Characters on source")
plt.ylabel("Frequency")
plt.xticks(lab_pos,labels)
plt.show()
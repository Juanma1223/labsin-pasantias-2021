# Converting domains into vowels and consonants
# Converts url domains into an array of characters occurrence

import csv
import numpy as np
from collections import Counter

initial_character = ord("#")
last_character = ord("{")
f = open('D:/Labsin/labsin-pasantias-2021/4_implementacion/converted_domains_to_my_model.csv','a+')
writer = csv.writer(f)

def calcEntropy(x):
    p, lens = Counter(x), np.float(len(x))
    return -np.sum( count/lens * np.log2(count/lens) for count in p.values())

# Counts vowels and consonants
def count(s):
    vowelCount = 0
    for vowel in "aeiou":
        vowelCount += s.count(vowel)
    tam = len(s)
    consonantCount = tam - vowelCount
    # Return vowel and count as well as domain length
    return [vowelCount,consonantCount,calcEntropy(s)]


# Write column names
col_names = ['vowels','consonants','entropy','label']
writer.writerow(col_names)

# Count vowels and consonants for each domain
with open('D:/Labsin/labsin-pasantias-2021/3_analisis/argencon_training_sample.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        characters_array = count(row['domain'])
        # Write the array and label at the end
        characters_array.append(row['label'])
        writer.writerow(characters_array)
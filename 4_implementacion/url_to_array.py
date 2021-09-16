# Converts url domains into an array of characters occurrence

import csv

initial_character = ord("#")
last_character = ord("{")
f = open('D:/Labsin/labsin-pasantias-2021/4_implementacion/converted_domains_to_array.csv','a+')
writer = csv.writer(f)

def count(s):
    global initial_character,last_character
    # Characters occurrence array
    counter = [0 for _ in range(0,last_character-initial_character)]
    for l in s:
        counter[ord(l)-initial_character] += 1
    return counter

'''
# Write column names
col_names = []
for i in range(0,last_character-initial_character):
    col_names.append(chr(i+initial_character))
col_names.append("label")
writer.writerow(col_names)
'''

# Write column names
col_names = []
for i in range(0,last_character-initial_character):
    col_names.append(i)
col_names.append("label")
writer.writerow(col_names)


# Count characters from each domain
with open('D:/Labsin/labsin-pasantias-2021/3_analisis/argencon_training_sample.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Count characters and get the array
        characters_array = count(row['domain'])
        # Write the array and label at the end
        characters_array.append(row['label'])
        writer.writerow(characters_array)
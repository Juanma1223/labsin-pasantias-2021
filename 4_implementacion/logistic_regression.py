from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pandas
import csv

# Open file which holds input data for the algorithm
df = pandas.read_csv("D:/Labsin/labsin-pasantias-2021/4_implementacion/converted_domains_to_array.csv")

initial_character = ord("#")
last_character = ord("{")

f = open('D:/Labsin/labsin-pasantias-2021/4_implementacion/argencon_sample_myalgo_domains_predictions.csv','a+')
writer = csv.writer(f)

def count(s):
    global initial_character,last_character
    # Characters occurrence array
    counter = [0 for _ in range(0,last_character-initial_character)]
    for l in s:
        counter[ord(l)-initial_character] += 1
    return counter

# Variables used to predict label
features = []
for i in range(0,last_character-initial_character):
    features.append(str(i))

X = df[features]

# Label to predict
y = df['label']

# Build logistic regression model
clf = LogisticRegression(random_state=0).fit(X, y)


################### Write predictions into file ##############################

# Write header
writer.writerow(['domain','label','label_pred','probability'])

# Test with sample and write predictions
with open('D:/Labsin/labsin-pasantias-2021/3_analisis/argencon_sample.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Get predicted label for current domain
        currDomain = row['domain']
        # Count letter distribution for domain
        charCount = count(currDomain)
        # Predict label for current domain
        label_pred = clf.predict([charCount])
        # Prediction correctness probability
        probability = clf.predict_proba([charCount])
        # Get probability 
        bestProb = max(probability[0])
        writer.writerow([currDomain,row['label'],label_pred[0],bestProb])
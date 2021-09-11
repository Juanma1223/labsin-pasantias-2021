# Uses requests library to perform http requests
import requests
import csv

# File to be written
f = open('D:/Labsin/labsin-pasantias-2021/3_analisis/argencon_sample_domains_predictions.csv','a+')
writer = csv.writer(f)

# Url to perform http requests
url = "http://ns158.ingenieria.uncuyo.edu.ar:8000/predict"

with open('D:/Labsin/labsin-pasantias-2021/3_analisis/argencon_sample.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    i = 0
    # Analyzing every domain with DGA prediction algorithm
    for row in reader:
        i += 1
        # Parameters used by get request
        params = {'domain' : row['domain']}
        # Perform get request
        try:
            prediction = requests.get(url = url, params = params)
        except Exception as e:
            print(e)
        # Parse to json
        data = prediction.json()
        # Creating new row
        newRow = [row['domain'],row['label'],row['date'],row['id'],data['class'],data['probability']]
        # Write on new file
        writer.writerow(newRow)
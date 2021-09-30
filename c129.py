import csv

data=[]
with open("dataset_2.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)

headers=data[0]
planet_data=data[1:]

for datapoint in planet_data:
    datapoint[2]=datapoint[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])

with open("dataset_2_sorted.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

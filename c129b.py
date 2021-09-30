import csv 

dataset_1=[]
dataset_2=[]

with open("dataset1.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)
        
with open("dataset_2_sorted.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

header1=dataset_1[0]
header2=dataset_2[0]
planet_data_1=dataset_1[1:]
planet_data_2=dataset_2[1:]
headers=header1+header2

planet_data=[]

for index,data_row in enumerate(planet_data_1):
    #print(index,data_row)
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open("final_2.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
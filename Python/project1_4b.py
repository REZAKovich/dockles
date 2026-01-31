import csv

filepath = 'F:\DevOps Курс\Python\orderdata_sample.csv'
filepathnew = 'F:\DevOps Курс\Python\orderdata_sample_new.csv'
data = []

with open(filepath,'r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

data[0].append('Total')

for i in range(1, len(data)):
    data[i].append(str(int(data[i][0]) * int(data[i][1]) + int(data[i][2])))

for i in data[1:]:
    if int(i[3]) > 10000:
        print(i[3])

with open(filepathnew,'a', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
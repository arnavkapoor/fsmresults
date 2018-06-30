import csv

rowscpu = []
rowsgpu = []

with open("cpuresultsnetwork1.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rowscpu.append(row)

with open("gpuresultsnetwork1.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rowscpures.append(row)

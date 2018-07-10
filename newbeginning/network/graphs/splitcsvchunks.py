import csv

rowsall = []

with open("gpuresultsnetworkchunks.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rowsall.append(row)

count=[]

a1=[]


print(rowsall)

for i in range(0,len(rowsall)-1):
	if(rowsall[i][0]==rowsall[i+1][0]):
		a1.append(rowsall[i])
	else:
		a1.append(rowsall[i])
		name=rowsall[i][0]
		file = csv.writer(open("./individualcsvchunks/"+name+".csv",'w'))
		file.writerow(['FSM','Testcases','Chunks','Total Time'])
		a1.sort(key=lambda x:(-int(x[1]),-int(x[2])))
		for elements in a1:
			print(elements) 
			file.writerow(elements)
		a1 = []
	
	if (i+2 == len(rowsall)):
		a1.append(rowsall[i+1])
		name=rowsall[i][0]
		file = csv.writer(open("./individualcsvldim/"+name+".csv",'w'))
		file.writerow(['FSM','Testcases','Chunks','Total Time'])
		a1.sort(key=lambda x:(-int(x[1]),-int(x[2])))
		for elements in a1:
			print(elements) 
			file.writerow(elements)
		a1 = []
		
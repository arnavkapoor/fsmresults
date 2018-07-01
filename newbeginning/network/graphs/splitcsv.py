import csv

rowsall = []

with open("mergednetwork.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rowsall.append(row)

count=[]

a1=[]


print(rowsall)
for i in range(1,len(rowsall)-1):
	if(rowsall[i][0]==rowsall[i+1][0]):
		a1.append(rowsall[i])
	else:
		a1.append(rowsall[i])
		name=rowsall[i][0]
		file = csv.writer(open("./individualcsv/"+name+".csv",'w'))
		file.writerow(['FSM', 'Testcases', 'Cores' ,'Total CPU' , 'Execution GPU', 'Total GPU']),
		for elements in a1:
			print(elements) 
			file.writerow(elements)
		a1 = []
	

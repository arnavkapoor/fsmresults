import csv

rowsall = []

with open("mergedresultsnetwork2.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rowsall.append(row)

count=[]

i=1
a1=[]
print(rowsall)
for i in range(0,len(rowsall)-1):
	if(rowsall[i][0]==rowsall[i+1][0]):
		a1.append(rowsall[i])
	else:
		name=rowsall[i][0]
		file = csv.writer(open("./individualcsv/"+name+"2.csv",'w'))
		file.writerow(['FSM', 'Testcases', 'Cores' ,'Total CPU' , 'Execution GPU Optimised', 'Total GPU Optimised' , 'Execution GPU Unoptimised', 'Total GPU Unoptimised']),
		for elements in a1:
			print(elements) 
			file.writerow(elements)
		a1 = []
	

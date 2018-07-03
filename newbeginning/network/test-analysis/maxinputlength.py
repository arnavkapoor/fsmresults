import os
import re
import sys
import csv

for file in os.listdir("./transition-pair-tests-network"):
    with open(os.path.join("./transition-pair-tests-network",file), 'r+') as fsmfile:
        basenm = file.split(".")[0]
        alllines = fsmfile.readlines()
        testsize=[]
        for lines in alllines:
            testsize.append(len(lines.split(" ")[1])- (3 * len(re.findall(r"\\[0-9][0-9][0-9]", lines.split(" ")[1]))) - len(re.findall(r"\n", lines.split(" ")[1])) - len(re.findall(r"\t", lines.split(" ")[1])) - len(re.findall(r"\a", lines.split(" ")[1])) ) 
        testsize.sort()
        numbers = []
        count = []
        pc = 1
        for i in range(len(testsize)-1):
            if ( testsize[i] == testsize[i+1] ):
                pc=pc+1
            else:
                numbers.append(testsize[i])
                count.append(pc)
                pc=1
        
        numbers.append(testsize[len(testsize)-1])
        count.append(pc)
        fraction = [ '{0:.10f}'.format(elements/len(testsize)) for elements in count]
        
        print(basenm)
        print(numbers)
        print(fraction)
        
        file = csv.writer(open("./individual-stats/"+basenm+".csv",'w'))
        file.writerow(['Length', 'Number','Percentage']),
        for i in range(0,len(numbers)):
            file.writerow([numbers[i],count[i],fraction[i]])


        
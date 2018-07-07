import os
import re
import sys
import csv

for file in os.listdir("../swiftsidecode/transition-pair-tests-network"):
    with open(os.path.join("../swiftsidecode/transition-pair-tests-network",file), 'r+') as fsmfile:
        basenm = file.split(".")[0]
        alllines = fsmfile.readlines()
        testsize=[]
        for lines in alllines:
          if len(lines.split(" ")) == 2: 
            string = lines.split(" ")[1]
            totallen = len(string)
            string = string.strip()
            escaped = ['a','b','t','n','v','f','r','\\']
            numbers = [ '0','1','2','3','4','5','6','7']
            i = 0
            while(i<len(string)):
                if(string[i] == '\\'):
                    try:
                        if(string[i+1] in escaped):
                            totallen = totallen - 1
                            i=i+1
                        else:
                            if(string[i+1] in numbers and string[i+2] in numbers and string[i+3] in numbers):
                                i=i+3
                                totallen = totallen - 3 
                    except:
                        pass 
                i=i+1        
            testsize.append(totallen) 
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


        
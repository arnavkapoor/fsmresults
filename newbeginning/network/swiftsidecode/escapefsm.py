import os
from pathlib import Path

for file in os.listdir("../allregexnew"):
    fsmdata = []
    with open(os.path.join("../allregexnew",file), 'r') as fsmfile:
        fsmdata=fsmfile.readlines()

    filewrite = open(os.path.join('../allregexfixed',file),"w")
    fsm = []
    print(file)
    for i in range(0,len(fsmdata)):
        fsm.append(fsmdata[i].strip().split())

    for elements in fsm:
        if(elements[0] == "\\"):
            elements[0]= r'\\'
            print(elements)        
    
    for elements in fsm:
        if(len(elements)==2):
            filewrite.write(elements[0] + " " +  elements[1] + '\n') 
        if(len(elements)==4):   
            filewrite.write(elements[0] + " " + elements[1] + " " + elements[2] + " "+ elements[3] + '\n')

import os
import re


directory = os.fsencode("./transition-pair-tests-network")

for file in os.listdir(directory):
    filepath = os.path.join(directory, file)
    with open(filepath,"r") as fsmfile:
        print(file)
        alllines=fsmfile.readlines()
        length=[]
        for lines in alllines:
            if len(lines.split(" ")) == 2: 
                length.append(len(lines.split(" ")[1])- (3 * len(re.findall(r"\\[0-9][0-9][0-9]", lines.split(" ")[1]))))
            else:
                length.append(len(lines.split(" ")[0])- (3 * len(re.findall(r"\\[0-9][0-9][0-9]", lines.split(" ")[0]))))
        length.sort()
        print(length[len(length)-1])

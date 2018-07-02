import os
import re
import sys
path = "./transition-pair-tests-network/"
path = path + sys.argv[1]
with open(path, 'r+') as fsmfile:
    alllines=fsmfile.readlines()
    length=[]
    for lines in alllines:
        if len(lines.split(" ")) == 2: 
            length.append(len(lines.split(" ")[1])- (3 * len(re.findall(r"\\[0-9][0-9][0-9]", lines.split(" ")[1]))) - len(re.findall(r"\n", lines.split(" ")[1])) - len(re.findall(r"\t", lines.split(" ")[1])) - len(re.findall(r"\a", lines.split(" ")[1])) ) 
        else:
            length.append(len(lines.split(" ")[0])- (3 * len(re.findall(r"\\[0-9][0-9][0-9]", lines.split(" ")[0]))) - len(re.findall(r"\n", lines.split(" ")[0])) - len(re.findall(r"\t", lines.split(" ")[0])) - len(re.findall(r"\a", lines.split(" ")[0])) )
    length.sort()
    print(length[len(length)-1])

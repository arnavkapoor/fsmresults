import sys
import itertools
import os
from collections import deque
fsm = []
prefixdict = {}
prefixlist = []

with open(sys.argv[1], 'r') as myfile1: # the fsm file
    fsmdata=myfile1.readlines()

with open(sys.argv[2],'r') as prefixfile:
    prefixdata=prefixfile.readlines()

for i in range(0,len(fsmdata)):
    fsm.append(fsmdata[i].strip().split())

for i in range(0,len(prefixdata)):
    prefixlist.append(prefixdata[i].strip().split())

for elements in prefixlist:
    if len(elements)>1:
        prefixdict[elements[0]]=elements[1]
    else:
        prefixdict[elements[0]]=""

namefile=(sys.argv[1].rsplit('/',1)[1])
filewrite= open(os.path.join('/afs/inf.ed.ac.uk/user/v/v1akapoo/fsm/tests/transition-pair-tests-network',namefile),"w")

userinput = []
currstate = []
nextstate = []
useroutput = []

visited = []
valid_digits = []
wildcard_compare = []

for ele in fsm:
    
    if(len(ele) == 2):
        if(ele[0] == '.b'):
            base = int(ele[1]) 
        if(ele[0] == '.p'):
            totalcount = int(ele[1])
        if(ele[0] == '.i'):
            inputlen = int(ele[1])
        if(ele[0] == '.o'):
            outputlen = int(ele[1])
                
    if(len(ele)==4):
        userinput.append(ele[0])
        currstate.append(ele[1])
        nextstate.append(ele[2])
        useroutput.append(ele[3])
        visited.append(0)

for i in range(0,len(currstate)):
    currstate[i] = int(currstate[i],base=base) # currstate[i] was initially string,converted to integer   

for i in range(0,len(nextstate)):
    nextstate[i] = int(nextstate[i],base=base)

x = len(userinput)


for i in range(x-1,-1,-1):
    
    inp = userinput[i]
    op = useroutput[i]
    cs = currstate[i]
    ns = nextstate[i]
    vs = visited[i]

testcases = []
print(namefile)
for i in range(0,len(userinput)):
    cs = currstate[i]
    try:
    	testcases.append(prefixdict[str(cs)]+userinput[i])
    except:
    	print("not reachable")
    		
for i in range(0,len(testcases)):
    filewrite.write(str(i+1) + " " + testcases[i] + '\n' )

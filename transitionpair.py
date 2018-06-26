import sys
import itertools
from collections import deque
fsm = []

with open(sys.argv[1], 'r') as myfile1: # the fsm file
    fsmdata=myfile1.readlines()


for i in range(0,len(fsmdata)):
    fsm.append(fsmdata[i].strip().split())


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

for i in range(0,base):
    valid_digits.append(i) # list containing (0,1,2,...b-1)

for i in itertools.product(valid_digits,repeat=inputlen):
    wildcard_compare.append(i)

x = len(userinput)

def compare(comp,s): 
    wild_present = False
    valid = True
   
    for i in range(0,len(comp)):
        if(comp[i] == "-"):
            wild_present = True

        if(comp[i] != str(s[i]) and comp[i] != "-" ):
            valid = False
    
    if(wild_present == True and valid == True):
        return True

    return False     

for i in range(x-1,-1,-1):
    
    inp = userinput[i]
    op = useroutput[i]
    cs = currstate[i]
    ns = nextstate[i]
    vs = visited[i]

    if "-" in inp:
        userinput.pop(i)
        useroutput.pop(i)
        currstate.pop(i)
        nextstate.pop(i)
        visited.pop(i)
        for s in range(0,len(wildcard_compare)):
            if(compare(inp,wildcard_compare[s])):
                x = ''.join(map(str,wildcard_compare[s]))
                userinput.append(x)
                useroutput.append(op)
                currstate.append(cs)
                nextstate.append(ns)
                visited.append(vs)

inout = {}

for ele in currstate:
    inout[ele]=([],[])

    
for i in range(0,len(userinput)):
    cs = currstate[i]
    ns = nextstate[i]
    ip = userinput[i]

    inout[cs][1].append((ns,ip))    # 1 is for out 
    inout[ns][0].append((cs,ip))    # 0 is for in
count = {}

for key,value in inout.items():
    count[key] = (len(value[0]),len(value[1]))
    for item_in in value[0]:
        for item_out in value[1]:
            inp = item_in[1] + item_out[1] 
            cs = item_in[0]
            ns = item_out[0]
            print(inp,cs,ns,"000000") 
total = 0
for key,value in count.items():
    total += value[0]*value[1]
print(total,"- total transitions ")

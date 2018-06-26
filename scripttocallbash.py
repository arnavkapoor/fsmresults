import sys
import itertools
import time
from subprocess import Popen, PIPE

fsm = []
test = []

with open(sys.argv[1], 'r') as myfile1: # the fsm file
    fsmdata=myfile1.readlines()

with open(sys.argv[2], 'r') as myfile2: # the test-case file 
    testcases=myfile2.readlines()

for i in range(0,len(fsmdata)):
    fsm.append(fsmdata[i].strip().split())

for i in range(0,len(testcases)):
    test.append(testcases[i].strip().split())

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

print(len(userinput),len(useroutput),len(currstate),len(nextstate))
listtest = [] 
 
for tests in test:
    listtest.append([tests[1],0])
 

#listtest contains the testcases. 
count = 0

def ispresent(userip,userop,currentst,nextst):
    global count
    for i in range(0,len(userinput)):
         if(userip == userinput[i] and userop == useroutput[i] and int(currentst) == currstate[i] and int(nextst) == nextstate[i]):
            if visited[i] == 0:
               visited[i]=1
               count += 1                
            return True
    return False

testtime=[]
start = time.time()

for i in range(0,len(listtest)):
    print (i)
    # Calling the bash program , with second argument being the input testcase
    #start = time.time()
    output = Popen(["/home/arnav/fsm/trial.sh", sys.argv[1] ,listtest[i][0]], stdout=PIPE) 
    #end = time.time()
    #testtime.append(end-start)
    
        #  stdout for some files 1 in a 1000 were being read before being written (some issue in synchronous
        #  read-write) running those files again solved the problem hence the while loop checking
        #  empty files. 
    final = output.stdout.readlines()
    while(len(final)==0): 
        start = time.time()
        output = Popen(["../a.out", sys.argv[1] , listtest[i][0] ], stdout=PIPE)
        end = time.time()
        testtime[i]+=end-start
        final = output.stdout.readlines()
    print(final)    

end = time.time()
print(end-start)

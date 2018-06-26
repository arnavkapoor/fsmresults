import sys
import itertools
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

testused=[]

for i in range(0,len(listtest)):
    myvar = i
    if count != len(userinput): 
        mycount = count
        thisop = []
        # Running the C program , with second argument being the input testcase
        output = Popen(["../a.out", sys.argv[1] ,listtest[i][0]], stdout=PIPE) 
        
        ip = listtest[i][0] #ip -- input test case
        final = output.stdout.readlines()
        
        #  stdout for some files 1 in a 1000 were being read before being written (some issue in synchronous
        #  read-write) running those files again solved the problem hence the while loop checking
        #  empty files. 
        
        while(len(final)==0): 
            output = Popen(["../a.out", sys.argv[1] ,listtest[i][0]], stdout=PIPE)
            final = output.stdout.readlines()
        
        for i in range(0,len(final)):
            thisop.append(final[i].strip().split())
        
        for i in range(0,len(thisop)):
            for j in range(0,len(thisop[i])):
                thisop[i][j] = thisop[i][j].decode('ascii')
        
        #print(thisop)
       # print(ip)
            
        invalid_index = [] #the list of index of input for which no transition is possible
        
        if(len(thisop[-1]) == 0):
            break
        
        op = thisop[-1][0]
        for i in range(1,len(thisop)-1):
            if(thisop[i][0] == "No"):
                invalid_index.append(i-1)

        print(op)        
        inputchunk = len(ip)
        outputchunk = len(op)
        
        inputs = [ ip[i:i+inputlen] for i in range(0, inputchunk, inputlen) ]
        outputs = [ op[i:i+outputlen] for i in range(0, outputchunk, outputlen)]
        
        invalid_index.sort(reverse=True)

        for elements in invalid_index:
            inputs.pop(elements)  
        
        x = 0
        currpointer = 0
        nextpointer = 1
        
        while( x < len(outputs) ):
            copy_count = count
            currentst = thisop[currpointer][0]
            nextst = thisop[nextpointer][0]    
            userip = inputs[x]
            userop = outputs[x]
            
            if(currentst == "No"):
                currpointer+=1

            if(nextst == "No" or nextpointer == currpointer):
                nextpointer+=1
                
            if(nextst != "No" and currentst != "No"):         
                 if(ispresent(userip,userop,currentst,nextst)):
                    x+=1
                    currpointer+=1
                    nextpointer+=1
        
        if(mycount < count):
            testused.append(myvar)        
    else:
        break        


# for i in range(0,len(currstate)):
#      print(userinput[i],currstate[i],nextstate[i],useroutput[i],visited[i])

# print("total tests used were",len(testused)," these are")
# print(testused)



# if(count != len(userinput)):
#     print("Add more tests to explore all Transitions")
#     print("current branch coverage percent = ",(count/len(userinput))*100)
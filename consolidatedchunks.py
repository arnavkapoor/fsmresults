import os,csv,re
path2 = '/home/arnav/fsmresults/gputestresultschunked'

file2 = csv.writer(open('gpuresultschunked.csv', 'w'))
file2.writerow(['FSM', 'Testcases', 'Chunks' , 'Execution GPU', 'Total GPU']),

for folder, sub_folders, files in os.walk(path2):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        with open(file_path, 'r+') as read_file:
            count = 0
            totaltime = []
            exectime = []
            for line in read_file:
                line=line.split()
                try:
                    float(line[0])
                    float(line[1])
                    float(line[2])
                    float(line[3])
                    count+=1
                    totaltime.append(float(line[3]))
                    exectime.append(float(line[2]))
                except:
                    pass   
            
            special_file=special_file.split('_')  
            manipulate = special_file[1][5:]
            #print(manipulate)
            chunks = (re.sub("\D", "", manipulate)) 
            fsmname = manipulate.lstrip('0123456789')
            print(manipulate,chunks)    
            totaltime.sort()
            exectime.sort()
            if count != 0 and count == 11 and special_file[0]!= "0":
               file2.writerow([fsmname,special_file[0],chunks,exectime[5],totaltime[5]])

import os,csv
path = '/home/arnav/fsmresults/cputestresultsswiftoptimum'
path2 = '/home/arnav/fsmresults/gputestresultsswift'


file = csv.writer(open('cpuresultsoptimumnetwork.csv', 'w'))
file.writerow(['FSM', 'Testcases', 'Cores', 'Total CPU']),

for folder, sub_folders, files in os.walk(path):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        with open(file_path, 'r+') as read_file:
            count = 0
            time = []
            for line in read_file:
                try:
                    float(line)
                    count+=1
                    time.append(float(line))
                except:
                   pass    
            special_file=special_file.split('_')        
            time.sort()
            if count == 11 and special_file[0]!= "0":
                file.writerow([special_file[2],special_file[0],special_file[1],time[5]])

file2 = csv.writer(open('gpuresultsnotoptimumnetwork.csv', 'w'))
file2.writerow(['FSM', 'Testcases', 'Execution GPU', 'Total GPU']),

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
            totaltime.sort()
            exectime.sort()
            if count != 0 and count == 11 and special_file[0]!= "0":
                file2.writerow([special_file[1],special_file[0],exectime[5],totaltime[5]])

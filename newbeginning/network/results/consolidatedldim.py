import os,csv
path = '../newrawdata/gputestresultsnetworkldim'
neededfiles = ['aim.test','battlefield2.test','counterstrike-source.test','dns.test','h323.test','halflife2-deathmatch.test','hotline.test','ntp.test','rtp.test','ssl.test','tsp.test','yahoo.test']
file = csv.writer(open('../graphs/gpuresultsnetworkldim.csv', 'w'))
file.writerow(['FSM','No_of_testcases','LDIM','Total Time'])
for folder, sub_folders, files in os.walk(path):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        with open(file_path, 'r+') as read_file:
            totaltime = []
            count = 0
            for line in read_file:
                line=line.split()
                try:
                    float(line[0])
                    float(line[1])
                    float(line[2])
                    float(line[3])
                    count+=1
                    totaltime.append(float(line[2]))
                except:
                    pass   
            special_file=special_file.split('_')  
            totaltime.sort()
            if count == 31 and special_file[0]!= "0" and special_file[2] in neededfiles:
                file.writerow([special_file[2],special_file[0],special_file[1],totaltime[count//2]])

# file2 = csv.writer(open('../graphs/gpuresultsnetwork.csv', 'w'))
# #file2.writerow(['Fsm', 'No_of_testcases', 'Execution Time', 'Total Time taken']),

# for folder, sub_folders, files in os.walk(path2):
#     for special_file in files:
#         file_path = os.path.join(folder, special_file)
#         with open(file_path, 'r+') as read_file:
#             count = 0
#             totaltime = []
#             exectime = []
#             for line in read_file:
#                 line=line.split()
#                 try:
#                     float(line[0])
#                     float(line[1])
#                     float(line[2])
#                     float(line[3])
#                     count+=1
#                     totaltime.append(float(line[3]))
#                     exectime.append(float(line[2]))
#                 except:
#                     pass   
#             special_file=special_file.split('_')  
#             totaltime.sort()
#             exectime.sort()
#             if count == 31 and special_file[0]!= "0" and special_file[1] in neededfiles:
#                 file2.writerow([special_file[1],special_file[0],exectime[5],totaltime[5]])

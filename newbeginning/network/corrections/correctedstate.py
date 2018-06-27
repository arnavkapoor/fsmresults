import os
path = '/home/arnav/fsmresults/newbeginning/network/fsmanalysis/data/allregexnew'
for folder, sub_folders, files in os.walk(path):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        filename=file_path.rsplit('/')[-1]
        with open(file_path, 'r+') as read_file:
            states = 0
            for line in read_file:
                line = line.strip().split()
                if(len(line) == 4):
                    states = max(states,int(line[1]),int(line[2]))
            print(states,filename)
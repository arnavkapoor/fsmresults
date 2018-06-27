import os,csv,math
path = '/home/arnav/fsmresults/newbeginning/opensource/opensrcexpanded'
for folder, sub_folders, files in os.walk(path):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        with open(file_path, 'r+') as read_file:
            totalnetwork= 255
            d=dict()
            for line in read_file:
                line = line.strip().split()
                if(len(line)==2):
                    if line[0] == ".i":
                        totalnetwork = math.pow(2,int(line[1]))
                if(len(line) == 4):
                    if line[1] not in d:
                        d[line[1]] = 1
                    else:
                        d[line[1]] += 1

        filename=file_path.rsplit('/')[-1]
        file = csv.writer(open('/home/arnav/fsmresults/newbeginning/opensource/fsmanalysis/results/' + filename + ".csv", 'w'))
        file.writerow(['State', 'Transitions', 'Percentage Transitions'])
        for key,values in d.items():
            file.writerow([key,values,values/totalnetwork])
            

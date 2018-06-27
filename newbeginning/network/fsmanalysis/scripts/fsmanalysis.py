import os,csv
totalnetwork= 255
path = '/home/arnav/fsmresults/newbeginning/network/fsmanalysis/data/allregexnew'
for folder, sub_folders, files in os.walk(path):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        with open(file_path, 'r+') as read_file:
            d=dict()
            for line in read_file:
                line = line.strip().split()
                if(len(line) == 4):
                    if line[1] not in d:
                        d[line[1]] = 1
                    else:
                        d[line[1]] += 1

        filename=file_path.rsplit('/')[-1]
        file = csv.writer(open('/home/arnav/fsmresults/newbeginning/network/fsmanalysis/data/results/' + filename + ".csv", 'w'))
        file.writerow(['State', 'Transitions', 'Percentage Transitions'])
        for key,values in d.items():
           file.writerow([key,values,values/totalnetwork])
           
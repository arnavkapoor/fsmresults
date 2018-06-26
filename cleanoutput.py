import os
path = '/home/arnav/fsm/tests/fsmresults/gputestresults'

for filename in os.listdir(path):
	with open(filename) as oldfile, open('newfile.txt', 'w') as newfile:
	    for line in oldfile:
	        if 'transition' not in line:
	            newfile.write(line)
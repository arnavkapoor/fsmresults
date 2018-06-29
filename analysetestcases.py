
import os

for filename in os.listdir('/home/arnav/fsmresults/transition-pair-tests-network'):
	print(filename)
	testdata = []
	with open('/home/arnav/fsmresults/transition-pair-tests-network/'+filename, 'r') as myfile1: # the test file
		testdata=myfile1.readlines()
	min=0
	max=0
	total=0
	count=len(testdata)

	for i in range(0,len(testdata)):
		print(type(testdata[i]))
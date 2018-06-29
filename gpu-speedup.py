# prints a speedup graph for multiple benchmark applications, across different test sizes 
# the data for each benchmark should be in a separate file, with the following format:
#
# Takes data in the following format:
# aiifft01
# trans-inputs trans-results exec-kernel speedup
# 0.10 0.027648 19.37056 1.84
# 0.28 0.052352 22.72736 3.08
# 0.68 0.1056 22.966848 6.08
# 2.10 0.511552 23.735808 11.78
# 3.17 0.751936 26.812896 20.84
# 8.14 1.593152 58.503872 19.18
# 17.10 3.500096 94.251552 23.66
# 33.55 6.08112 166.381984 26.48
# 72.83 14.454784 311.900768 28.20
# 143.89 28.00176 618.686016 28.10

import numpy
import argparse
import itertools
from utils import getbmrkname, getdatafiles
import matplotlib as mplt
mplt.rcParams['ps.useafm'] = True
mplt.rcParams['pdf.use14corefonts'] = True
mplt.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt 

parser = argparse.ArgumentParser()
parser.add_argument('datafiledir', help='speedup data for applications')
args = parser.parse_args()

#find all data files in the directory
directory = args.datafiledir
datafiles = getdatafiles(directory)

testsizes = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]

#create handle combinations
linestyles = ['-', ':', '-.', '--']
markers = ['x', '^', 'o', '*']
handlestyles = itertools.product(linestyles, markers)

#used to sort the legend based on the highest speedup
sortingpoints = []
labels = []
handles = []

rowidxmaxtestsuite = 9
colidxkernelwithoverlap = 3
colidxnooverlap = 4

fig, ax = plt.subplots()
ax.set_xscale('log', basex=2)

#plot the data
for datafile in datafiles:
    print(datafile)
    label = getbmrkname(datafile)
    data = numpy.loadtxt(datafile, skiprows=2)
    handlestyle = next(handlestyles)
    plotdata =  data[:,colidxnooverlap]
    handle, = plt.plot(testsizes, plotdata, linestyle=handlestyle[0], lw = 2, label=label, marker=handlestyle[1], markersize=20, linewidth=4) 
    #store legend data
    sortingpoints.append(plotdata[rowidxmaxtestsuite])
    labels.append(label)
    handles.append(handle)

#draw line at 1
plt.axhline(y=1, c='k', linewidth=1)

#change tick frequency of ticks of the y axis
start, end = ax.get_ylim()
plt.yticks(list(plt.yticks()[0])+[1], fontsize=15)
ax.yaxis.grid(True, which='1')

#plt.title('GPU Speedup', fontsize ='large')
plt.xlabel('Number of tests (log base 2)',  fontsize=40)
plt.ylabel('GPU speedup when compared to a single CPU', fontsize =40)
plt.yticks(fontsize=30)
plt.xticks(testsizes,fontsize=30)

#sort the labels/handles by the sorting points
sortingpoints, labels, handles = zip(*sorted(zip(sortingpoints, labels, handles), key=lambda t: t[0], reverse=True))
#set the legend
plt.legend(loc = 2, fontsize =35, labels=labels, handles=handles)

fig=plt.figure()

plt.show()

# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF

import math
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 
neededfiles = ['aim.test','battlefield2.test','counterstrike-source.test','dns.test','h323.test','halflife2-deathmatch.test','hotline.test','ntp.test','rtp.test','ssl.test','tsp.test','yahoo.test']
names = ['cpu1','cpu8','cpu16','cpu32','gpuexec','gputotal']

speedup32 = []
speedup16 = []
speedup8 = []
executiongpu = []
bmklist = []
totalgpu = []

for filename in neededfiles:
    df = pd.read_csv('./individualcsv/'+filename+'.csv')
    totalcpu = (df['Total CPU'].values.tolist())
    timecpu1 = totalcpu[3]    

    speedup32.append(timecpu1/totalcpu[0])
    speedup16.append(timecpu1/totalcpu[1])
    speedup8.append(timecpu1/totalcpu[2])
    
    bmk = filename.split('.')[0]
    bmklist.append(bmk)
    
    executiongpu.append( timecpu1/(df['Execution GPU'].drop_duplicates().values.tolist()[0]))
    totalgpu.append( timecpu1/(df['Total GPU'].drop_duplicates().values.tolist()[0]))
    
N = len(bmklist)
fig,ax = plt.subplots()
ind = np.arange(N)
width=0.10


p1 = ax.bar(ind,speedup8, width, color='r')
p2 = ax.bar(ind+width,speedup16, width, color='y')
p3 = ax.bar(ind+2*width,speedup32, width, color='g')
p4 = ax.bar(ind+3*width,totalgpu, width, color='b')
p5 = ax.bar(ind+4*width,executiongpu, width, color='m')

ax.set_title('Speed-up in Execution Time')

ax.set_xticks(ind + 2*width)
ax.set_xticklabels(bmklist,rotation=20)
ax.legend((p1[0], p2[0],p3[0],p4[0]), ('Cpu8', 'Cpu16','Cpu32','Gpu Unoptimised'))
plt.ylabel("Speed up compared to single core CPU")
plt.show()


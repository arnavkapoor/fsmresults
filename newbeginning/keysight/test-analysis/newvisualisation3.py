# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF

import math
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 
neededfiles = ['aim.fsm','battlefield2.fsm','counterstrike-source.fsm','dns.fsm','halflife2-deathmatch.fsm','h323.fsm','hotline.fsm','ntp.fsm','rtp.fsm','ssl.fsm','tsp.fsm','yahoo.fsm']
src1='./individualcsvdense2_char1/'
src2='./individualcsvdense2sorted_char1/'
src3='./fsmstats.csv'

df2 = pd.read_csv(src3)
names = (df2['FSM'].values.tolist())
speedup = []
average = (df2['Average all'].values.tolist())  

for filename in neededfiles:

    filename=filename.split('.')[0]
    df = pd.read_csv(src1+filename+'.test.csv')
    df1 = pd.read_csv(src2+filename+'.test.csv')
    
    time = df['Execution GPU'].values.tolist()[5]
    numtc = df['Testcases'].values.tolist()[5]
    speedup.append(numtc/time)

zipped = list(zip(names,average,speedup))
zipped.sort(key = lambda t: t[1])

names,average,speedup = zip(*zipped)
#plt.xticks(names)

names=list(names)
average=list(average)
speedup=list(speedup)

print(names,average,speedup)
plt.xticks(np.arange(int(average[0]), int(average[-1]), step=1),names)

plt.plot(average,speedup)
plt.show()
# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF
import csv
import math
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 
neededfiles = ['keysight-1000.csv']
file = csv.writer(open("fsmstats.csv",'w'))
file.writerow(['FSM', 'Median', 'Standard Deviation' ,'Variance','Average all','Total all'])      

for filename in neededfiles:
    filename=filename.split('.')[0]
    df = pd.read_csv('./individual-stats/'+filename+'.csv')
    #df2 = pd.read_csv('./individual-stats-2pow20/'+filename+'.csv')
    
    freq =df['Number'].values.tolist()
    val = df['Length'].values.tolist()
    
    #freq2 =df2['Number'].values.tolist()
    #val2 = df2['Length'].values.tolist()
    
    bmk = filename
    
    data = np.repeat(val, freq)
    #data2 = np.repeat(val2, freq2)
    
    tsumtot=0
    #tsumtot2=0
    
    for ele in data:
        tsumtot+=ele
        
    #for ele2 in data2:
    #    tsumtot2+=ele2

    file.writerow([bmk,np.median(data),np.std(data),np.var(data),np.average(data),tsumtot])
  

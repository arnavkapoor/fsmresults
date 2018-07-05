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
neededfiles = ['aim.fsm','battlefield2.fsm','counterstrike-source.fsm','halflife2-deathmatch.fsm','dns.fsm','h323.fsm','hotline.fsm','ntp.fsm','rtp.fsm','ssl.fsm','tsp.fsm','yahoo.fsm']
file = csv.writer(open("fsmstats.csv",'w'))
file.writerow(['FSM', 'Median', 'Standard Deviation' ,'Variance'])        

for filename in neededfiles:
    filename=filename.split('.')[0]
    df = pd.read_csv('./individual-stats/'+filename+'.csv')
    freq =df['Number'].values.tolist()
    val = df['Length'].values.tolist()
    bmk = filename
    data = np.repeat(val, freq)
    file.writerow([bmk,np.median(data),np.std(data),np.var(data)])
  

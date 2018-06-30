import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import math
import numpy as np
import pandas as pd
df = pd.read_csv('../speedup2.csv')
testcases=(df['Test-Cases'].values.tolist())
speedup = (df['Speedup'].values.tolist())
fsm=(df['Fsm'].values.tolist())
logtestcases = [ math.log(element,2) for element in testcases ]
lengthfsm=[0]
namefsm=[]
k=0
for i in range(0,len(fsm)-1):
    if fsm[i]!=fsm[i+1]:
        lengthfsm.append(i+1)
        namefsm.append(fsm[i])
d1=dict()    
d2=dict()
for i in range(0,len(lengthfsm)-1):
    d1[namefsm[i]] =  speedup[lengthfsm[i]:lengthfsm[i+1]]
    d2[namefsm[i]] =  logtestcases[lengthfsm[i]:lengthfsm[i+1]]

print(d1)
print(d2)

print(len(lengthfsm))
print(len(namefsm))
print(len(logtestcases))
dataPanda=[]

for i in range(0,len(namefsm)//2):
    
    trace = go.Scatter(
         x=d2[namefsm[i]],
         y=d1[namefsm[i]],
         mode='lines+markers',
         name=namefsm[i]
    )
    dataPanda.append(trace)

layout ={
    	'yaxis': {
        'title' : 'Speed-Up Factor'
        },
        'shapes':[ {
            'type': 'line',
            'x0': 0,
            'y0': 1,
            'x1': 20,
            'y1': 1,
            'line': {
                'width': 1,
                'dash': 'dot',
            },
        },
        ]
 }
fig = dict(data=dataPanda,layout=layout)
py.iplot(fig, filename='grouped-bar')
py.image.save_as(fig, 'speedupoptvsnotopt.png')

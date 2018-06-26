import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import math
import numpy as np
import pandas as pd
df = pd.read_csv('aimsubplot.csv')

testcases=(df['Test-Cases'].drop_duplicates().values.tolist())
totalcpu = (df['Total CPU'].values.tolist())
logtestcases = [ math.log(element,2) for element in testcases ]

totalcpu32=[]
totalcpu8=[]
totalcpu4=[]
totalcpu1=[]

for i in range(0,len(totalcpu)):
    if(i%4==0):
        totalcpu32.append(totalcpu[i])
    if(i%4==1): 
        totalcpu8.append(totalcpu[i])
    if(i%4==2):
        totalcpu4.append(totalcpu[i])
    if(i%4==3):
        totalcpu1.append(totalcpu[i])

executiongpu = (df['Execution GPU'].drop_duplicates().values.tolist())
totalgpu = (df['Total GPU'].drop_duplicates().values.tolist())
print(totalcpu1,logtestcases)
trace1 = go.Bar(
    x=logtestcases,
    y=totalcpu1,
    name='1 cpu core'
)

trace2 = go.Bar(
    x=logtestcases,
    y=totalcpu4,
    name='4 cpu cores'
)


trace3 = go.Bar(
    x=logtestcases,
    y=totalcpu8,
    name='8 cpu cores'
)

trace4 = go.Bar(
    x=logtestcases,
    y=totalcpu32,
    name='32 cpu cores'
)

trace5 = go.Bar(
    x=logtestcases,
    y=totalgpu,
    name='gpu total'
)


trace6 = go.Bar(
    x=logtestcases,
    y=executiongpu,
    name='gpu execution'
)

data = [trace1, trace2,trace3,trace4,trace5,trace6]
layout = go.Layout(
    yaxis=dict(
        title="time taken in ms"
        ),
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
#py.iplot(fig, filename='grouped-bar')
py.image.save_as(fig, 'aimfsmsubplot.png')
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import math
import numpy as np
import pandas as pd
df = pd.read_csv('../individualcsv/all500k.csv')


testcases=(df['Fsm'].drop_duplicates().values.tolist())
totalcpu = (df['Time taken'].drop_duplicates().values.tolist())

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

executiongpuop = (df['Execution GPU Optimised'].drop_duplicates().values.tolist())
totalgpuop = (df['Total GPU Optimised'].drop_duplicates().values.tolist())

executiongpunop = (df['Execution GPU Unoptimised'].drop_duplicates().values.tolist())
totalgpunop = (df['Total GPU Unoptimised'].drop_duplicates().values.tolist())

#print(testcases,totalgpu,executiongpu)

trace1 = go.Bar(
    x=testcases,
    y=totalcpu1,
    text=testcases,
    name='1 cpu core'
)

trace2 = go.Bar(
    x=testcases,
    y=totalcpu4,
    text=testcases,
    name='4 cpu cores'
)


trace3 = go.Bar(
    x=testcases,
    y=totalcpu8,
    text=testcases,
    name='8 cpu cores'
)

trace4 = go.Bar(
    x=testcases,
    y=totalcpu32,
    text=testcases,
    name='32 cpu cores'
)

trace5 = go.Bar(
    x=testcases,
    y=totalgpuop,
    name='gpu total Optimised'
)


trace6 = go.Bar(
    x=testcases,
    y=executiongpuop,
    name='gpu execution Optimised'
)

trace7 = go.Bar(
    x=testcases,
    y=totalgpunop,
    name='gpu total Unoptimised'
)

trace8 = go.Bar(
    x=testcases,
    y=executiongpunop,
    name='gpu execution Unoptimised'
)

data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8]

layout = go.Layout(
   	yaxis=dict(
   		title="time taken in ms"
   		),
    barmode='group'

)

fig = go.Figure(data=data, layout=layout)
#py.iplot(fig, filename='grouped-bar')
py.image.save_as(fig, '1048576_test_across_fsm(1).png')
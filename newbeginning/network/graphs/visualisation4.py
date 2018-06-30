import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import math
import numpy as np
import pandas as pd
df = pd.read_csv('./individualcsv/aim.test.csv')

testcases=(df['Testcases'].drop_duplicates().values.tolist())
totalcpu = (df['Total CPU'].values.tolist())
totalcpu32=[]
totalcpu16=[]
totalcpu8=[]
totalcpu1=[]

for i in range(0,len(totalcpu)):
    if(i%4==0):
        totalcpu32.append(totalcpu[i])
    if(i%4==1): 
        totalcpu16.append(totalcpu[i])
    if(i%4==2):
        totalcpu8.append(totalcpu[i])
    if(i%4==3):
        totalcpu1.append(totalcpu[i])

names = []

executiongpuop = (df['Execution GPU Optimised'].drop_duplicates().values.tolist())
totalgpuop = (df['Total GPU Optimised'].drop_duplicates().values.tolist())
allaboard = []
for i in range(0,len(testcases)):
    totalcpu1[i] = (testcases[i]/totalcpu1[i])*1000
    totalcpu8[i] = (testcases[i]/totalcpu8[i])*1000
    totalcpu16[i] = (testcases[i]/totalcpu16[i])*1000
    totalcpu32[i] = (testcases[i]/totalcpu32[i])*1000
    executiongpuop[i] = (testcases[i]/executiongpuop[i])*1000
    totalgpuop[i] = (testcases[i]/totalgpuop[i])*1000

allaboard.append(totalcpu1,totalcpu8,totalcpu16,totalcpu32,executiongpuop,totalgpuop)


dataPanda=[]

for i in range(0,len(allaboard)):
    trace = go.Scatter(
         x=testcases,
         y=allaboard[i],
         mode='lines+markers',
         name=names[i]
    )
    dataPanda.append(trace)

layout ={
        'yaxis': {
        'title' : 'Testcases/second'
        },
        'xaxis': {
        'title' : 'Number of Testcases'
        },
 }

fig = dict(data=dataPanda,layout=layout)
py.iplot(fig, filename='grouped-bar')
py.image.save_as(fig, '../individualgraphs/aimgraph.png')



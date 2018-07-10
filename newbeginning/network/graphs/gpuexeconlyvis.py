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

mplt.rc('xtick', labelsize=12) 
mplt.rc('ytick', labelsize=12) 

linestyles = ['-', ':', '-.', '--']
markers = ['x', '^', 'o', '*']
handlestyles = itertools.product(linestyles, markers)    

handles = []
labels = []
sortingpoints = []
  
for filename in neededfiles:
    df = pd.read_csv('./individualcsv/'+filename+'.csv')
    testcases=(df['Testcases'].drop_duplicates().values.tolist())
    totalcpu = (df['Total CPU'].values.tolist())
    totalcpu32=[]
    totalcpu16=[]
    totalcpu8=[]
    totalcpu1=[]
    logtestcases = [ math.log(element,2) for element in testcases ]
    bmk = filename.split('.')[0]
    #create handle combinations
    
    #print(handlestyles)
    
    for i in range(0,len(totalcpu)):
        if(i%4==0):
            totalcpu32.append(totalcpu[i])
        if(i%4==1): 
            totalcpu16.append(totalcpu[i])
        if(i%4==2):
            totalcpu8.append(totalcpu[i])
        if(i%4==3):
            totalcpu1.append(totalcpu[i])

    myindices = []

    executiongpupre = (df['Execution GPU'].values.tolist())
    totalgpupre = (df['Total GPU'].values.tolist())
    
    for i in range(0,len(executiongpupre)):
        if i%4 == 0:
            myindices.append(i)

    executiongpu  = [ executiongpupre[i] for i in myindices ]  
    totalgpu  = [ totalgpupre[i] for i in myindices ]       
    for i in range(0,len(executiongpu)):
        executiongpu[i] = totalcpu1[i]/executiongpu[i]


    handlestyle = next(handlestyles)
    handle,=plt.plot(logtestcases,executiongpu,label=bmk,linestyle=handlestyle[0],marker=handlestyle[1])
    handles.append(handle)
    labels.append(bmk)
    sortingpoints.append(executiongpu[0])

plt.ticklabel_format(style = 'plain',labelsize=10)
plt.ylabel('Speed up compared to single core CPU',fontsize=15)
plt.xlabel('Number of tests (log base 2)',fontsize=15)

    #sort the labels/handles by the sorting points
sortingpoints, labels, handles = zip(*sorted(zip(sortingpoints, labels, handles), key=lambda t: t[0], reverse=True))
    #set the legend
plt.legend(loc = 2, fontsize = 15, labels=labels, handles=handles)
#plt.title(bmk,fontsize=15)
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
#plt.savefig('./newsetofgraphs/'+'dense2char1'+'.pdf',bbox_inches='tight')
plt.show()
#plt.close()
    #plt.show()    
    # layout ={
    #         'title':filename,
    #         'yaxis': {
    #         'title' : 'Testcases/second'
    #         },
    #         'xaxis': {
    #         'title' : 'Log Number of Testcases'
    #         },
    #  }

    # fig = dict(data=dataPanda,layout=layout)
    # py.image.save_as(fig, './individualgraphs/'+filename+'2.png')


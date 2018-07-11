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
    linestyles = ['-', ':', '-.', '--']
    markers = ['x', '^', 'o', '*']
    handlestyles = itertools.product(linestyles, markers)
    
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

    names = ['cpu1','cpu8','cpu16','cpu32','gpuexec','gputotal']
    myindices = []

    executiongpupre = (df['Execution GPU'].values.tolist())
    totalgpupre = (df['Total GPU'].values.tolist())
    
    for i in range(0,len(executiongpupre)):
        if i%4 == 0:
            myindices.append(i)
    executiongpu  = [ executiongpupre[i] for i in myindices ]  
    totalgpu  = [ totalgpupre[i] for i in myindices ]       

    allaboard = []
    print(len(testcases))
    for i in range(0,len(testcases)):
        totalcpu1[i] = (testcases[i]/totalcpu1[i])*1000/1000000
        totalcpu8[i] = (testcases[i]/totalcpu8[i])*1000/1000000
        totalcpu16[i] = (testcases[i]/totalcpu16[i])*1000/1000000
        totalcpu32[i] = (testcases[i]/totalcpu32[i])*1000/1000000
        executiongpu[i] = (testcases[i]/executiongpu[i])*1000/1000000
        totalgpu[i] = (testcases[i]/totalgpu[i])*1000/1000000

    allaboard.extend([totalcpu1,totalcpu8,totalcpu16,totalcpu32,executiongpu,totalgpu])
    print(allaboard)
    
    dataPanda=[]
    handles = []
    labels = []
    sortingpoints = []

    for i in range(0,len(allaboard)):
        handlestyle = next(handlestyles)
        handle,=plt.plot(logtestcases,allaboard[i],label=names[i],linestyle=handlestyle[0],marker=handlestyle[1])
        handles.append(handle)
        labels.append(names[i])
        print("sorting by",allaboard[i][0])
        sortingpoints.append(allaboard[i][0])

    plt.ticklabel_format(style = 'plain')
    plt.ylabel('Number of testcases (in millions) per second')
    plt.xlabel('Number of tests (log base 2)',  fontsize=10)

    #sort the labels/handles by the sorting points
    sortingpoints, labels, handles = zip(*sorted(zip(sortingpoints, labels, handles), key=lambda t: t[0], reverse=True))
    #set the legend
    plt.legend(loc = 2, fontsize = 10, labels=labels, handles=handles)
    plt.title(bmk,fontsize=15)
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    #plt.show()
    plt.savefig('./individualgraphs/'+bmk+'.svg',bbox_inches='tight',dpi=1000)
    plt.close()
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


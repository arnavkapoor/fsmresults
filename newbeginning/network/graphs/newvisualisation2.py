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
    df = pd.read_csv('./individualcsvldim/'+filename+'.csv')
    testcases=(df['Testcases'].drop_duplicates().values.tolist())
    totalgpu = (df['Total Time'].values.tolist())
    totalgpu1024=[]
    totalgpu512=[]
    totalgpu256=[]
    totalgpu128=[]
    totalgpu64=[]
    totalgpu32=[]

    logtestcases = [ math.log(element,2) for element in testcases ]
    bmk = filename.split('.')[0]
    #create handle combinations
    linestyles = ['-', ':', '-.', '--']
    markers = ['x', '^', 'o', '*']
    handlestyles = itertools.product(linestyles, markers)
    
    #print(handlestyles)
    
    for i in range(0,len(totalgpu)):
        if(i%6==0):
            totalgpu1024.append(totalgpu[i])
        if(i%6==1): 
            totalgpu512.append(totalgpu[i])
        if(i%6==2):
            totalgpu256.append(totalgpu[i])
        if(i%6==3):
            totalgpu128.append(totalgpu[i])
        if(i%6==4):
            totalgpu64.append(totalgpu[i])
        if(i%6==5):
            totalgpu32.append(totalgpu[i])
        
    names = ['ldim1024','ldim512','ldim256','ldim128','ldim64','ldim32']
    print(filename)
    print(totalgpu32,totalgpu64)
    allaboard = []
    for i in range(0,len(testcases)):
        totalgpu1024[i] = (testcases[i]/totalgpu1024[i])*1000
        totalgpu512[i] = (testcases[i]/totalgpu512[i])*1000
        totalgpu256[i] = (testcases[i]/totalgpu256[i])*1000
        totalgpu128[i] = (testcases[i]/totalgpu128[i])*1000
        totalgpu64[i] = (testcases[i]/totalgpu64[i])*1000
        totalgpu32[i] = (testcases[i]/totalgpu32[i])*1000

    allaboard.extend([totalgpu1024,totalgpu512,totalgpu256,totalgpu128,totalgpu64,totalgpu32])
    
    dataPanda=[]
    handles = []
    labels = []
    sortingpoints = []

    for i in range(0,len(allaboard)):
        handlestyle = next(handlestyles)
        handle,=plt.plot(logtestcases,allaboard[i],label=names[i],linestyle=handlestyle[0],marker=handlestyle[1])
        handles.append(handle)
        labels.append(names[i])
        sortingpoints.append(allaboard[i][0])

    plt.ticklabel_format(style = 'plain')
    
    plt.ylabel('Number of testcases per second')
    plt.xlabel('Number of tests (log base 2)',  fontsize=10)

    #sort the labels/handles by the sorting points
    sortingpoints, labels, handles = zip(*sorted(zip(sortingpoints, labels, handles), key=lambda t: t[0], reverse=True))
    #set the legend
    plt.legend(loc = 2, fontsize = 10, labels=labels, handles=handles)
    plt.title(bmk,fontsize=15)
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    #plt.show()
    plt.savefig('./individualgraphsldim/'+bmk+'.png',bbox_inches='tight')
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


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
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
    
print(plt.get_backend())
for filename in neededfiles:
    df = pd.read_csv('./individualcsvchunks/'+filename+'.csv')
    df2 = pd.read_csv('./individualcsv/'+filename+'.csv')
    df3 = pd.read_csv('./individualcsvoffset/'+filename+'.csv')
    

    totalcpu32 = (df2['Total CPU'].values.tolist()[0])
    totalcpu16 = (df2['Total CPU'].values.tolist()[1])
    totalcpu8 = (df2['Total CPU'].values.tolist()[2])
    totalcpu1 = (df2['Total CPU'].values.tolist()[3])

    numchunks = (df['Chunks'].values.tolist()) 
    totalgpu = (df['Total Time'].values.tolist())
    bmk = filename.split('.')[0]
    #create handle combinations
    linestyles = ['-', ':', '-.', '--']
    markers = ['x', '^', 'o', '*']
    handlestyles = itertools.product(linestyles, markers)
    for i in range(0,len(totalgpu)):
        totalgpu[i] = round((totalcpu1/totalgpu[i]),2)
    #print(handlestyles)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for xy in zip(numchunks,totalgpu):
        ax.annotate(xy[0], xy=xy, textcoords='data')


    plt.plot(numchunks,totalgpu,marker='x',label='GPU Pipeline')
    
    plt.axhline(y=(totalcpu1/totalcpu32),color='k',label='32 core-cpu')
    plt.axhline(y=(totalcpu1/totalcpu16),c='y',label='16 core-cpu')
    plt.axhline(y=(totalcpu1/totalcpu8),c='c',label='8 core-cpu')

    plt.axhline(y=(totalcpu1/(df2['Total GPU'].values.tolist()[0])),ls='dashdot',c='r',label='GPU no-pipeline')    
   # plt.axhline(y=(totalcpu1/(df2['Execution GPU'].values.tolist()[0])),ls='dashdot',c='m',label='GPU no-chunking char1 execution time')    
  #  plt.axhline(y=(totalcpu1/(df3['Total GPU'].values.tolist()[0])),ls='dotted',c='g',label='GPU offset total time')
    
    plt.legend(loc="upper right")
    plt.ylabel('Speedup compared to single core CPU')
    plt.xlabel('Size of Chunks in KB',  fontsize=10)
    #sort the labels/handles by the sortng points
    plt.title(bmk,fontsize=15)
    #plt.show()
    plt.savefig('./individualgraphschunks/'+bmk+'.png',bbox_inches='tight')
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


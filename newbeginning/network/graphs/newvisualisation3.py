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
    df = pd.read_csv('./individualcsvchunks/'+filename+'.csv')
    tc = (df['Testcases'].values.tolist()) 
    
    numchunks = (df['Chunks'].values.tolist()) 
    totalgpu = (df['Total Time'].values.tolist())
    exectime = (tc[0]/totalgpu[4])*1000
    del totalgpu[4] 
    del numchunks[4]
    bmk = filename.split('.')[0]
    #create handle combinations
    linestyles = ['-', ':', '-.', '--']
    markers = ['x', '^', 'o', '*']
    handlestyles = itertools.product(linestyles, markers)
    for i in range(0,len(totalgpu)):
        totalgpu[i] = (tc[0]/totalgpu[i])*1000
    #print(handlestyles)
    
    plt.plot(numchunks,totalgpu)
    plt.axhline(y=exectime)


    plt.ylabel('Number of testcases per second')
    plt.xlabel('Number of Chunks',  fontsize=10)

    #sort the labels/handles by the sorting points
    plt.title(bmk+"("+str(tc[0])+")",fontsize=15)
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
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


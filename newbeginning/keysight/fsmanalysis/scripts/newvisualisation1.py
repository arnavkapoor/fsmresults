# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF

import math
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 
neededfiles = ['aim.fsm','battlefield2.fsm','counterstrike-source.fsm','dns.fsm','h323.fsm','hotline.fsm','ntp.fsm','rtp.fsm','ssl.fsm','tsp.fsm','yahoo.fsm']

for filename in neededfiles:
    df = pd.read_csv('../data/'+filename+'.csv')
    testcases=(df['Percentage Transitions'].values.tolist())
    bmk = filename.split('.')[0]
    #create handle combinations
    # linestyles = ['-', ':', '-.', '--']
    # markers = ['x', '^', 'o', '*']
    # handlestyles = itertools.product(linestyles, markers)
    testcases.sort()
    x = [i for i in range(1,len(testcases)+1)]
    plt.bar(x,testcases,align='center')
    plt.ylabel('Transition Percentage', fontsize=10)
    plt.xlabel('States',  fontsize=10)

    plt.title(bmk,fontsize=15)
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    #plt.show()
    plt.savefig('../individualgraphs/'+bmk+'.png')
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


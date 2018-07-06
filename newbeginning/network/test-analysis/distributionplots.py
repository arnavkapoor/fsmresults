# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF

import math
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set(color_codes=True)
neededfiles = ['aim.fsm','battlefield2.fsm','counterstrike-source.fsm','halflife2-deathmatch.fsm','dns.fsm','h323.fsm','hotline.fsm','ntp.fsm','rtp.fsm','ssl.fsm','tsp.fsm','yahoo.fsm']

for filename in neededfiles:
    filename=filename.split('.')[0]
    df = pd.read_csv('./individual-stats/'+filename+'.csv')
    freq=(df['Percentage'].values.tolist())
    vals = df['Length'].values.tolist()
    bmk = filename
    print(freq)
    #create handle combinations
    # linestyles = ['-', ':', '-.', '--']
    # markers = ['x', '^', 'o', '*']
    # handlestyles = itertools.product(linestyles, markers)
    gaussian = sns.kdeplot(freq,shade=True,bw=2)
    
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
    plt.xticks(np.arange(vals[0], vals[-1], step=1))
    fig = gaussian.get_figure()
    fig.savefig('./individualgraphspercent/'+bmk+"gaussian.svg",dpi=1000)
    # fig = dict(data=dataPanda,layout=layout)
    # py.image.save_as(fig, './individualgraphs/'+filename+'2.png')


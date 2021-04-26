import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def calculate_time_axis(traces):
    min_time=traces[0]["begin_time"]
    max_time=traces[0]["begin_time"]+traces[0]["delta"]*len(traces[0]["data"])
    for i in range(1,len(traces)):
        t0=traces[i]["begin_time"]
        t1=traces[0]["delta"]*len(traces[i]["data"])
        if t0<min_time:
            min_time=t0        
        if t0+t1>max_time:
            max_time=t1+t0
    return [min_time,max_time]

###------------------------------------------
def plot_wiggle(traces,fig=None, ori='v',norm="trace", color='k', scale=0.5, verbose=False):
    '''Wiggle plot of a sesimic data section
    add parameter ori(orientation):
        v: verticle
        h: horizontal
    add parameter norm (normalization method):
        trace: normalize by trace
        all: normalize by the max element of 
    rename sf(scale factor) to scale

    Syntax examples:
        wiggle(data)
        wiggle(data, tt)
        wiggle(data, tt, xx)
        wiggle(data, tt, xx, color)
        fi = wiggle(data, tt, xx, color, scale, verbose)
    '''

    if not fig:
        fig=plt.figure()
        ax = fig.add_subplot()
    else:
        ax = fig.add_subplot()

    xx = np.arange(len(traces))  ##using 

    # Compute trace horizontal spacing
    #ts = np.min(np.diff(xx))

    # Rescale data by trace_spacing and strech_factor
    if norm=="trace":
        for i in range(0, len(traces)):
            
            traces[i]["data"] = traces[i]["data"]/np.max(traces[i]["data"])*scale

    elif norm=="all":
        pass
    
    ntraces=len(traces)
    time_range=calculate_time_axis(traces)
    print("time_range=", time_range)
    for i in range(len(traces)):
        trace = traces[i]
        offset = i
        tt=[]
        for j in range(0,len(trace["data"])):
            t0=j*trace["delta"]+trace["begin_time"]
            tt.append(t0)

        if ori=='v':            
            ax.set_xticks (xx)
            ax.set_ylim(time_range)
            ax.plot(trace["data"] + offset, tt, color)
            ax.fill_betweenx(tt, offset,trace["data"] + offset, where=trace["data"]>0,facecolor=color)
            
        elif ori=='h':
            ax.set_yticks (xx)
            ax.set_xlim(time_range)
            ax.plot(tt, trace["data"] + offset, color)
            ax.fill_between(tt, offset, trace["data"] + offset, where=trace["data"]>0, facecolor=color) 
    if ori=="v":
        ax.invert_yaxis() 
    add_button(ax)
    return ax

def addButtonCallBack():

def add_button(ax ):
    xmin,xmax=ax.get_xlim()
    callback = Index()
    add_scale = plt.axes([(xmax-xmin)/2, 0, 0.1, 0.075])
    axnext = plt.axes([0.81, 0, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Previous')
    bprev.on_clicked(callback.prev)

if __name__ == '__main__':
    trace1={"delta":0.1, "begin_time":5, "data":np.random.randn( 100)}
    trace2={"delta":0.1, "begin_time":0, "data":np.random.randn( 100)}
    plot_wiggle([trace1, trace2], ori='v',color='red')
    plt.show()
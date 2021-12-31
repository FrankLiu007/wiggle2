import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons,RangeSlider,RadioButtons
import copy
class wiggle:
    def __init__(self, traces=None, ori='v', norm="trace", scale=0.5 ):
        self.traces=traces

        self.ori=ori
        self.norm=norm

        self.scale=scale
        self.fig=plt.figure(111,(8,6))
        self.wiggle_axis=None
        #plt.subplots_adjust(left=0.2)

        self.amplitude_slider=None
        self.negative_fill_enabled=False
        self.negative_fill_color=None
        self.positive_fill_enabled = True
        self.positive_fill_color = "black"

        self.add_amplitude_slider()
        self.add_checkbuttons()
        self.tmp_traces=copy.copy(traces)
        self.update_traces()

    def add_checkbuttons(self):

        rax1 = plt.axes( [0.05, 0.5, 0.1, 0.3])
        plt.title("Positive Fill Color")
        self.radio = RadioButtons(rax1, ('None', 'black', 'red', 'blue', 'gray'), (False,True,False, False, False))
        self.positive_fill_enabled=True
        self.radio.on_clicked(self.positive_wiggle_fill)

        rax2 = plt.axes([0.05, 0.1, 0.1, 0.3])
        plt.title("Nagative Fill Color")
        self.radio2 = RadioButtons(rax2, ('None', 'black', 'red', 'blue', 'gray'), (False,True,False, False, False))
        self.negative_fill_enabled = True
        self.radio2.on_clicked( self.negative_wiggle_fill)

    def positive_wiggle_fill(self,label):


        self.positive_fill_color = label
        if label=="None":
            self.positive_fill_color=None
        self.plot_wiggle()
        plt.draw()

    def negative_wiggle_fill(self,label  ):

        self.negative_fill_color = label
        if label=="None":
            self.negative_fill_color=None
        self.plot_wiggle()
        plt.draw()

    def add_amplitude_slider(self):
        ax = plt.axes([0.2, 0.9, 0.5, 0.05])
        self.amplitude_slider = Slider(
            ax=ax,
            label="Amplitude",
            valmin=0,
            valmax=5,
            valinit=1
        )
        self.amplitude_slider.on_changed(self.update_scale)
    def update_scale(self,val):
        self.scale=self.amplitude_slider.val
        self.update_traces()
        self.plot_wiggle()

    def update_traces(self):
        ntraces = len(self.traces)

        if self.norm=="trace":
            for i in range(0, ntraces):
                self.tmp_traces[i]["data"] = self.traces[i]["data"]/np.max(self.traces[i]["data"]) * self.scale

        elif self.norm=="all":
            pass

    def calculate_time_axis(self):
        traces=self.traces
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
    def plot_wiggle(self):
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


        if self.wiggle_axis:
            plt.axis('off')
            self.wiggle_axis = None

        self.wiggle_axis=self.fig.add_subplot()
        plt.subplots_adjust(left=0.2)

        xx = np.arange(len(self.traces))  ##using



        time_range=self.calculate_time_axis()

        for i, trace in enumerate(self.tmp_traces):

            offset = i
            tt=[]
            for j in range(0,len(trace["data"])):
                t0=j*trace["delta"]+trace["begin_time"]
                tt.append(t0)

            if self.ori=='v':
                self.wiggle_axis.set_xticks (xx)
                self.wiggle_axis.set_ylim(time_range)
                self.wiggle_axis.plot(trace["data"] + offset, tt, color="black")
                if self.negative_fill_color :
                    self.wiggle_axis.fill_betweenx(tt, offset,trace["data"] + offset, where=trace["data"]<0,facecolor=self.negative_fill_color)
                if self.positive_fill_color:
                    self.wiggle_axis.fill_betweenx(tt, offset,trace["data"] + offset, where=trace["data"]>0,facecolor=self.positive_fill_color)

            elif self.ori=='h':
                self.wiggle_axis.set_yticks (xx)
                self.wiggle_axis.set_xlim(time_range)
                self.wiggle_axis.plot(tt, trace["data"] + offset, color="black")
                if self.negative_fill_color:
                    self.wiggle_axis.fill_between(tt, offset, trace["data"] + offset, where=trace["data"]<0, facecolor=self.negative_fill_color)
                if self.positive_fill_color:
                    self.wiggle_axis.fill_between(tt, offset, trace["data"] + offset, where=trace["data"]>0, facecolor=self.positive_fill_color)

        if self.ori=="v":
            self.wiggle_axis.invert_yaxis()


if __name__ == '__main__':

    traces=[]
    for i in range(0,50):
        trace={"delta":0.1, "begin_time":5, "data":np.random.randn( 100)}
        traces.append(trace)
    wig=wiggle(traces, ori='v')
    wig.plot_wiggle()
    plt.show()
#wiggle2

## Wiggle Plot for Seismic Data by liu qimin 

![Alt text](screenshot.png "ScreenShot")


## Introduction
Utility to plot seismic data, inspired by [wiggle](https://github.com/lijunzh/wiggle) function.
I provide more options, such as orientation, normalization method, scale. 
This tool used fillbetween and fillbetweenx in the matplotlib package

## Dependancy
- [NumPy](http://www.numpy.org/)
- [Matplotlib](http://matplotlib.org/)

## Installation
### From PyPI
```
pip install wiggle2
```

### From source file
Download srouce file from [releases page](https://github.com/gatechzhu/wiggle/releases). Under the root directory, type:

```
python setup.py install
```
### Ussage
```
from wiggle2 import wiggle
import numpy as np
import matplotlib.pyplot as plt

traces=[]
for i in range(0,50):
    trace={"delta":0.1, "begin_time":5, "data":np.random.randn( 100)}
    traces.append(trace)
wig=wiggle(traces, ori='v')
wig.plot_wiggle()
plt.show()

```
### Problems
> 1. Sometimes the plot takes too much time
> 2. 

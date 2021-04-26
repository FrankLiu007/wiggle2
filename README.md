#Large modification of 

# Wiggle Plot for Seismic Data Section

[![Build Status](https://travis-ci.org/gatechzhu/wiggle.svg?branch=master)](https://travis-ci.org/gatechzhu/wiggle)

## Introduction
Utility to plot seismic data, inspired by [wiggle](https://github.com/lijunzh/wiggle) function.
I provide more options, such as orientation, normalization method, scale. 

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
trace1={"delta":0.1, "begin_time":5, "data":np.random.randn( 100)}
trace2={"delta":0.1, "begin_time":0, "data":np.random.randn( 100)}

ax=wiggle.plot_wiggle([trace1, trace2], ori='v',color='red')
plt.show()
```


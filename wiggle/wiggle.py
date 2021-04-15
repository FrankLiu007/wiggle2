import numpy as np
import matplotlib.pyplot as plt

def wiggle_input_check(data, tt, xx, scale, verbose):
    ''' Helper function for wiggle() and traces() to check input

    '''
    # Input check for verbose
    if not isinstance(verbose, bool):
        raise TypeError("verbose must be a bool")

    # Input check for data
    if type(data).__module__ != np.__name__:
        raise TypeError("data must be a numpy array")

    if len(data.shape) != 2:
        raise ValueError("data must be a 2D array")

    # Input check for tt
    if tt is None :
        if type(tt).__module__ != np.__name__:
            raise TypeError("tt must be a numpy array")
        if len(tt.shape) != 1:
            raise ValueError("tt must be a 1D array")
        if tt.shape[0] != data.shape[0]:
            raise ValueError("tt must have same as data's rows")

    # Input check for xx
    if not (xx is None) :
 
        if type(xx).__module__ != np.__name__:
            raise TypeError("tt must be a numpy array")
        if len(xx.shape) != 1:
            raise ValueError("tt must be a 1D array")
        if tt.shape[0] != data.shape[1]:
            raise ValueError("tt must have same as data's rows")
        if verbose:
            print(xx)

    # Input check for streth factor (scale)
    if not isinstance(scale, (int, float)):
        raise TypeError("Strech factor(scale) must be a number")


    return True


def wiggle(data, tt=None, xx=None,ori='v',norm="trace", color='k', scale=0.2, verbose=False):
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
    if xx is None:
        xx = np.arange(data.shape[0])
        if verbose:
            print("xx is automatically generated.")
            print(xx)
    if tt is None:
        tt = np.arange(data.shape[1])
        if verbose:
            print("tt is automatically generated.")
            print(tt)
    # Input check
    wiggle_input_check(data, tt, xx, scale,verbose)
    

    # Compute trace horizontal spacing
    ts = np.min(np.diff(xx))

    # Rescale data by trace_spacing and strech_factor
    if norm=="trace":
        for i in range(0, data.shape[0]):
            print("max=", np.max(data[i,:]))
            data[i,:] = data[i,:]/np.max(data[i,:])*scale
            #data = data / data_max_std * ts * scale
    elif norm=="all":
        data=data/data.max()*ts*scale

    # Plot data using matplotlib.pyplot
    Ntr = data.shape[0]

    ax = plt.gca()

    for ntr in range(Ntr):
        trace = data[ ntr,:]
        
        offset = xx[ntr]

        if verbose:
            print(offset)

        if ori=='v':
            ax.plot(trace + offset, tt, color)
            ax.fill_betweenx(tt, offset,trace + offset, where=trace>0,facecolor=color)
            
        elif ori=='h':
            ax.plot(tt, trace + offset, color)
            ax.fill_between(tt, offset, trace + offset, where=trace>0, facecolor=color) 
    if ori=="v":
        ax.invert_yaxis()    


if __name__ == '__main__':
    data = np.random.randn(10, 100)
    wiggle(data, ori='v',color='red')
    plt.show()
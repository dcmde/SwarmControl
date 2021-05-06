import numpy as np

def square_well(x,y,limits):
    return (np.exp(-x+limits[0])-np.exp(x-limits[1]),
            np.exp(-y+limits[2])-np.exp(y-limits[3]))

def point_source(x,y,x0,y0,gain):
    return (gain*(2*(x-x0)/np.power(np.power(x-x0,2)+np.power(y-y0,2),2)),
            gain*(2*(y-y0)/np.power(np.power(x-x0,2)+np.power(y-y0,2),2)))

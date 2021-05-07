import numpy as np

# θ should be in the interval [-π,π]
def line(x,ρ,θ):
    ρ = np.abs(ρ)
    if θ > -np.pi/4 and θ < np.pi/4 or θ < -3*np.pi/4 or θ > 3*np.pi/4:
        θ += np.pi/2
        y = -x/np.tan(θ) + ρ/np.sin(θ)
        return (y,-x)
    else:
        y = -x/np.tan(θ) + ρ/np.sin(θ)
        return (x,y)

def square_well(x,y,limits):
    return (np.exp(-x+limits[0])-np.exp(x-limits[1]),
            np.exp(-y+limits[2])-np.exp(y-limits[3]))

def point_source(x,y,x0,y0,α):
    return (α*(2*(x-x0)/np.power(np.power(x-x0,2)+np.power(y-y0,2),2)),
            α*(2*(y-y0)/np.power(np.power(x-x0,2)+np.power(y-y0,2),2)))

def line_source(x,y,ρ,θ,α):
    None
    
    
    

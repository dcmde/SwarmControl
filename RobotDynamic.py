import numpy as np

A = np.array([[-1,0,0,0],[0,-1,0,0],[1,0,0,0],[0,1,0,0]])
B = np.array([[1,0],[0,1],[0,0],[0,0]])
I = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
Te = 0.01
F = I+A*Te
G = B*Te

# Drone State Space Equations
def DroneSys(xk,uk):
    xk = np.resize(xk,(4,1))
    uk = np.resize(uk,(2,1))
    return F@xk + G@uk

import numpy as np 

#Function to draw a circle
def circle(phi,r):
    return np.array([r*np.cos(phi), r*np.sin(phi)])
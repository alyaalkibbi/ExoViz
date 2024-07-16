import numpy as np 

#A function defining an ellipse
#inputs are angle (phi), semi-major axis (a),
# and eccentricity (e)
def ellipse(phi,a,e):
    b = np.sqrt(1-e**2) * a 
    return np.array([a*np.cos(phi), b*np.sin(phi)])


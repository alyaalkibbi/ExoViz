import numpy as np 
import matplotlib.pyplot as plt 

def color(teff):
    if teff < 3500:
        return 'red'

    if teff >= 3500 & teff < 5000:
        return 'orange'
    
    if teff >= 5000 & teff < 8000:
        return 'yellow'
    
    if teff >= 8000 & teff < 15000:
        return 'white'
    
    if teff >= 15000:
        return 'blue'
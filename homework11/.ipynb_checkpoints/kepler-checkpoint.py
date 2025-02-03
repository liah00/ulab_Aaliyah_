#File: kepler.py
import numpy as np

def keplers_law(axis):
    time = (axis**3)**(1/2)
    return time
    """
    Returns the orbital period
    of a planet.
    Inputs: semi-major axis
    Outputs: orbital period
    """
    
    time = (axis**3)**(1/2)
    return time
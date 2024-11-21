#File: cos_sin.py
import numpy as np
import matplotlib.pyplot as plt

def left_right_subplot(x):
    """
    Plots a sine and cosine function on subplot next to each other
    Inputs: domain for x
    Outputs: sine and cosine curve 
    """
    y1 = np.sin(x)
    y2 = np.cos(x)
    fig, ax = plt.subplots (1,2,figsize=(10,10))
    ax[0].plot(x,y2)
    ax[0].set_title("cosine")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    
    ax[1].plot(x,y1)
    ax[1].set_title("sine")
    ax[1].set_xlabel("x-axis")
    ax[1].set_ylabel("y-axis")

    plt.show()
    return 

def up_below_subplot(x):
    """
    Plots a sine and cosine function on subplots, one below the other
    Inputs: domain for x
    Outputs: sine and cosine curve
    """
    y1 = np.sin(x)
    y2 = np.cos(x)
    fig, ax = plt.subplots (2,1,figsize=(10,10))
    ax[0].plot(x,y2)
    ax[0].set_title("cosine")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    
    ax[1].plot(x,y1)
    ax[1].set_title("sine")
    ax[1].set_xlabel("x-axis")
    ax[1].set_ylabel("y-axis")

    plt.show()
    return
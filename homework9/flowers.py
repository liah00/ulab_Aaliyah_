#File: flowers.py
import numpy as np
import matplotlib.pyplot as plt

def graphing_a_flower(n, chosen_color):
    """
    Plots a flower
    Inputs: color nd number of petals
    Outputs: flower curve  
    """
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(n*x)
    
    plt.figure(figsize= (10,10))
    ax1 = plt.subplot(111, projection='polar')
    ax1.plot(x, y, color = chosen_color)

    ax1.set_title("Polar Flower Plot")
    plt.show()
    return
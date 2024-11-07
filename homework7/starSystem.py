# File:other starSystem.py

import numpy as np

#constants
G = 6.6743e-11 # Gravitational contanst in m^3 kg^-1 s^-2
RS = 696000 #km
MS = 2e30 #kg
pi = 3.14

def how_far_away(parallax):
    """
    determines the distance to the system from earth
    
    Inputs:
    parallax angle (float): arcseconds

    Output:
    distance (float): parsec
    """
    
    distance = 1.0/parallax
    return distance

def what_star(radius, mass):
    """
    Determines how big the star is compared to our sun
    
    Inputs:
    mass (float): mass of the star in kg
    radius (float) :radius of the star in km

    Output:
    statement about size of the star compared to ours
    """
    heavier = ""
    bigger = ""

    mass /= MS
    radius /= RS

    if mass > MS:
        heavier = "The star is heavier than our sun."
    else:
        heavier = "The star is less massive than our sun."
        
    if radius > RS:
        bigger = "The star is larger than our sun."
    else:
        bigger = "The star is smaller than out sun."
        
    answer = "The star has a mass of " + str(mass) + " solar masses and a radius of " + str(radius) +" solar radii. " + heavier +" "+ bigger
    return answer 

def order_of_planets(Mass_star, planets, num):
    """
    Orders planets based on their distance to their star (ascending)
    
    Inputs:
    Mass_star (float): mass of the star in kg
    planets (2D rray): planet names, period (s), and mass (kg)
    num (int): number of total planets

    Output:
    odered ascending list of planet distamces 
    """
    order = []
    for i in range(num):
        P = float(planets[1][i])
        P2 = P**2
        tot_mass = Mass_star + float(planets[2][i])
        a3 = (P2*G*tot_mass)/(4*pi)
        a = a3**(1/3)
        a = np.round(a , 1)
        order.append(float(a))
    order.sort()
    return order 



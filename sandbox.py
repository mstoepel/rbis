"""
Created on Thu Aug 11 10:31:03 2016

@author: mstoepel
"""
# Test solar system.  3 planets (a, b, and c). 3 resources (x, y, and z). population of planet = pop
# Each planet needs a certain amount of x, y, and z based on their pop. will take from the resource
# pool until depleted. cost associated with taking resource based on distance from it. total wealth 
# will go down as planet gets necessary resource. New resources can be added to system 
# POPa = 5MM    POPb = 5MM  POPc =5MM
# Px = 50*d     Py = 25*d   Pz = 10*d   d = distance from planet to resource
# Dx = pop*2 - 1000Px    Dy = pop*3 - 1000Py  Dz = pop*10 - 1000Pz
# Sx = 100M     Sy = 500M   Sz = 2MM

def demand_fn(resource,planet):
    
def supply_fn(resource,planet):

def planet_a(Dx,Dy,Dz,pop,wealth): #Planet A's actions. Give inputs, it makes decisions and acts. Outputs
    

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

Sx1 = 100000
Sx2 = 30000
Sx3 = 456133
Sy1 = 500000
Sy2 = 123546
Sy3 = 846532
Sz1 = 2000000
Sz2 = 465433
Sz3 = 789654

POPa = 5000000
POPb = 5000000
POPc = 5000000

Wa = 25000000
Wb = 10000000
Wc = 75000000

Px = 500
Py = 250
Pz = 100

planet_a = (POPa,Wa,5,5) # Population, Wealth, x-coord, y-coord
planet_b = (POPb,Wb,25,15)
planet_c = (POPc,Wc,6,50)
resource_x1 = (Sx1,Px,10,16)
resource_x2 = (Sx2,Px,10,40)
resource_x3 = (Sx3,Px,20,3)
resource_y1 = (Sy1,Py,20,18)
resource_y2 = (Sy2,Py,33,49)
resource_y3 = (Sy3,Py,1,28)
resource_z1 = (Sz1,Pz,40,8)
resource_z2 = (Sz2,Pz,8,40)
resource_z3 = (Sz3,Pz,15,15)

def C(planet,resource):
    Cost = 0
    dist = math.hypot(planet[2]-resource[2] , planet[3]-resource[3])
    Cost = resource[1]*dist
    print Cost
    print dist
    
def D(planet,resource):
    demand = 0
    demand = planet[0] - 5000*resource[1]
    print demand
    
    
Cy = 25*d
Cz = 10*d

def demand_fn(resource,planet):

    
def supply_fn(resource,planet):

def planet_a(pop,wealth,x,y): #Planet A's actions. Give inputs, it makes decisions and acts. Outputs
    aDx = pop*2 - 1000*Px    
    
    
    
def resource_x(quantity,x,y):
    
    
planet_a
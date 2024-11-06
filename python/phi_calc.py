import numpy as np
import math


R = 104.85	
BoxA = math.pi*R*R

N = 2000 #10000 #50000 # number of particles
GA = 0.5*N*math.pi*(0.7*0.7 + 0.5*0.5)

phi = GA/BoxA

print( f'R = {R},  phi = {phi}' )
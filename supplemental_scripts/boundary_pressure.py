import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# Data folder
folder_name = 'my_1000particles/Equilibration' #'my_1000particles/Inflation/'# 
filename = 'dump-Kn200000-phi0.86-GammaN500-Reference-RadStep0.lammpstrj' #'dump-Kn200000-phi0.86-GammaN500-Inflate1.01-End.lammpstrj'# 



# constants
Kn_wall = 1.0e6#2.0e6#
R = 20.742 # radius of big circle

# radius & x location & y location
r_i = [] # r initial
x_i = []
y_i = []

path = folder_name + '/' + filename

with open(path) as f:
	for i in range(9):
		next(f)	
	# counter = 0
	for line in f:
		# counter += 1
		# print(counter)

		r_i.append( float(line.split()[2]) )
		x_i.append( float(line.split()[3]) )
		y_i.append( float(line.split()[4]) )
f.close()


# choose particles, that tounch big circle radius
r = [] # radius of particle near boundary
x = []
y = []
r_vector = []

for i in range( len(r_i) ):
	r_vector_all = math.sqrt(x_i[i]*x_i[i] + y_i[i]*y_i[i]) # radius-vector of a particle 

	if r_vector_all + r_i[i] >= R:
		r_vector.append( r_vector_all )
		r.append( r_i[i] )
		x.append( x_i[i] )
		y.append( y_i[i] )



# frictional force between two granular particles (the Hertzian style)

P = 0 # pressure
A = sum(i*i for i in r) # this is necessary for area of all particles near boundary

for i in range( len(r) ):
	x_wall = R * x[i]/r_vector[i] # x[i]/r_vector[i] = cos(theta); theta is an angle of radius-vector of a particle
	y_wall = R * y[i]/r_vector[i] # y[i]/r_vector[i] = sin(theta)
	
	dx = x_wall - x[i]
	dy = y_wall - y[i]

	dr = math.sqrt(dx*dx + dy*dy)
	delta =  r[i] - dr #R - dr

	nx = x[i]/r_vector[i] # normalized radius-vector 
	ny = y[i]/r_vector[i]

	sqrt_term = math.sqrt( -r[i]*R / (r[i] - R) )

	# fx = Kn_wall*(delta**(1.5))*nx*sqrt_term
	# fy = Kn_wall*(delta**(1.5))*ny*sqrt_term


	P += (delta**(1.5))*(x[i]*nx + y[i]*ny)*sqrt_term

	# print(f"r: {r[i]},    x: {x[i]},    y: {y[i]}\n")
	# print(f"nx = {nx},     ny = {ny}")
	# print(f"fx = {fx},     fy = {fy}")
	# print(f"xi = {x[i]},   x_wall = {x_wall},                yi = {y[i]},   y_wall = {y_wall}")
	# print(delta)


P = Kn_wall*P/(2*math.pi*A)

# f_writeto = open('results/boundary_pressure.dat', 'w')
# f_writeto.write(f'P = {P}')


print( P )

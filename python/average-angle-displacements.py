import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


phi = 0.836 # phi
press = 17.97 # pressure after inflation
R = 29.75 # the whole area radius
Na = 2000 # number of particles
Kn = 20000 # Kn value


# Data folder

folder_name = 'data/infl/Kn' + str(Kn) + '-phi' + str(phi) +'-GammaN500-Inflate1.01'
filename = 'dump-Kn' + str(Kn) + '-phi' + str(phi) + '-GammaN500-Inflate1.01-Disp-End.lammpstrj'


# particle positions 
x = []
y = []
# displacements 
dx = []
dy = []

path = folder_name + '/' + filename

with open(path) as f:
	for i in range(9):
		next(f)	

	for line in f:
		x.append(float(line.split()[1]))
		y.append(float(line.split()[2]))
		dx.append(float(line.split()[3]))
		dy.append(float(line.split()[4]))

f.close()

particle_number = len(x) # number of particles



# R = 147.569063 # the whole area radius
r_number = 50 # number of radii, on which angle-average displacements are searched
r = [None]*r_number # list of these radii


r[0] = R/r_number

for i in range(1, r_number):
	r[i] = r[i-1] + R/r_number

# del r[-1]

# print(r)

disp_list = [] # list of angle-average displacement
eps_pos = 0.5 # eps for defining particle position == minimal radius


for r_var in r[:-1]:

	part_counter = 0 # particle counter
	disp_sum = 0 # sum of displacement magnitude
	
	for i in range(particle_number):
		
		r_i = math.sqrt(x[i]*x[i] + y[i]*y[i])
		
		if abs( r_i - r_var ) <= eps_pos:
			disp_sum += ( dx[i]*x[i] + dy[i]*y[i] ) / r_i
			part_counter += 1
			
			# print( f'i = {i},    r_var = {r_var},    {part_counter}:  {disp_sum}' )
			# print( i )

	disp_list.append( disp_sum/part_counter )

disp_list.append(0) # for the last elemnt

# print(disp_list)

# print r and d to the file
f_writeto = open('results/displ_vs_r_Na='+str(Na)+'_Kn=' + str(Kn) + '_P='+str(press)+'.dat', 'w')

#f_writeto.write(str(len(r)) + "\n")
#f_writeto.write(str(len(disp_list)) + "\n")
#f_writeto.write(str(particle_number) + "\n")

f_writeto.write("#	radius	displacement\n")	
for i in range(r_number):
	f_writeto.write(str(i) + " " + str(r[i]) + "	" + str(disp_list[i]) + "\n")
f_writeto.close()
		

# draw plot
fig, axs = plt.subplots(figsize=(11, 7))

label = ("Na = " + str(Na) + 
	"\n"
	r"$\phi$ = " + str(phi) + 
	"\n"
	"P=" + str(press))
axs.plot( r, disp_list, lw=2, marker='o', label = label)

axs.axhline( y=0, color='green', linestyle='--' )
plt.xlabel('$r$', fontsize=20)
plt.ylabel('$displacements$', fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
axs.legend(fontsize=16, loc='best')

# interpolation
# label_interp = "interpolation"
# r_interp = np.linspace(r[0], r[-1], num=10000, endpoint=True)
# d_interp = interp1d(r, disp_list, kind='cubic')
# axs.plot(r_interp, d_interp(r_interp), lw=4, color="darkmagenta", label=label_interp)


folder_save = 'results'
name_save = 'Na=' + str(Na) + '_phi='+str(phi)+'_Kn='+str(Kn)+'_P='+str(press)

# plt.savefig(folder_save + '/' + name_save + '.pdf')

plt.show()



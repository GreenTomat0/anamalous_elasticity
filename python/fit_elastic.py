import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


press = 
phi = 0.836
r_out = 29.75
Na = 2000
Kn = 20
Knstr = '20'
alpha = 0.2
c2 = 1.98
Knwall = '5Kn'


# Data folder
#DIR = 'results/fixed_center/Kn' + Knstr + '/Na=' + str(Na) + '_phi=' + str(phi) + '_alpha=' + str(alpha) + '_Kn=' + str(Kn) + '_P=' + str(press)
DIR = 'results/fixed_center/Kn' + Knstr + '/Knwall' + Knwall + '/Na_' + str(Na) + '-phi_' + str(phi) + '-Kn_' + str(Kn) + '-alpha_' + str(alpha) + '-c2_' + str(c2)
filename = 'displ_vs_r_Na=' + str(Na) + '_alpha=' + str(alpha) + '_Kn=' + str(Kn) + '_P=' + str(press) +'.dat'

# radius & displacements
r = []
d = []

path = DIR + '/' + filename

with open(path) as f:
	next(f)	
	for line in f:
		r.append(float(line.split()[1]))
		d.append(float(line.split()[2]))
f.close()


# def fit_func(x, a, b, c):
#     return -a*(x**3) + b*x + c/x


def fit_func(x, a):
	return -a*x*(x*x - r_out*r_out)/(8.0*c2*c2*c2*c2)

params = curve_fit(fit_func, r, d)

# [a, b, c] = params[0]
[a] = params[0]

# print(r"a = ", a, "b = ", b, "c = ", c)
print(r"a = ", a)

print("min(r) = ", min(r), "max(r) = ", max(r))

# define a sequence of inputs between the smallest and largest known inputs
x_line = np.arange(0, r_out, 0.1) #np.arange(min(r), max(r))
# calculate the output for the range
# y_line = fit_func(x_line, a, b, c)
y_line = fit_func(x_line, a)



# draw plots
fig, axs = plt.subplots(figsize=(11, 7))

# ttext = f"Na = {Na}\n" + r"$\phi = $" + f"{phi}\nP = {press}\nc2 = {c2}\na = {a:.7f}"
# axs.text(30, 0.3, ttext, fontsize=16)

elastic_text = "quasielastic, " + f"a = {a:.7f}"
axs.plot( x_line, y_line, lw=3, ls='-', color="red", label=elastic_text )
axs.plot( r, d, lw=2, marker='o', ls="-", color="blue", label = "simulation")
# axs.plot( r, quasielastic, lw=2, marker='o', label = "quasielastic formula")

plt.xlabel('$r$', fontsize=20)
plt.ylabel('$d$', fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
axs.legend(fontsize=16, loc='best')

plt.title(r'$\alpha = $' + f'{alpha}', fontsize=22)


DIR = './summary/22-11-20'#'results/Kn=' + str(Kn) + '_Na=' + str(Na) + '_P=' + str(press)
# name_save = 'simulation_elastic_N=10K_phi=0.845_P=56_c2=1.9'
name_save = 'fit_elastic_Na=' + str(Na) + '_phi=' + str(phi) + '_P=' + str(press) + '_c2=' + str(c2)

# plt.savefig(DIR + '/' + name_save + '.jpg', dpi=100)


plt.show()
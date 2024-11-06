import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import j1


press = 3218.6
phi = 0.842
R = 29.65
Na = 2000
Kn = 200000
Knstr_dir = '2e5'
Knstr = '2e5'
alpha = 0.2
c2 = 1.9
# a = 0.001445711000408
# a_test = a
damp = 0.1
Knwall = '5Kn'
# nu = 0.3
# K = 0.1
# kappa_w = 0.1


# Data folder
#DIR = 'results/fixed_center/Kn' + Knstr + '/Na=' + str(Na) + '_phi=' + str(phi) + '_alpha=' + str(alpha) + '_Kn=' + str(Kn) + '_P=' + str(press)
DIR = 'results/fixed_center/Kn' + Knstr_dir + '/Knwall' + Knwall + '/Na_' + str(Na) + '-phi_' + str(phi) + '-Kn_' + Knstr_dir + '-alpha_' + str(alpha) + '-c2_' + str(c2)
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

# print(len(r))

def fit_elastic(x, a):
	return -a*x*(x*x - R*R)/(8.0*c2*c2*c2*c2)

params = curve_fit(fit_elastic, r, d)

[a] = params[0]

print(f'a = {a}')

x_line_e = np.arange(0, R, 0.1) #np.arange(min(r), max(r))#
y_line_e = fit_elastic(x_line_e, a)


def fit_anom(x, kappa_w):
	c2Sqr = c2*c2
	# j1 is the Bessel function of kind one, order 1
	return ( 1 - c2Sqr - a/(kappa_w*kappa_w*c2Sqr) )*(x*j1(kappa_w*R) - R*j1(kappa_w*x))/(c2Sqr*j1(kappa_w*R)) / 200
	# return ( 1 - c2Sqr - a/(kappa_w*kappa_w*c2Sqr) )*(R*j1(kappa_w*x) - x*j1(kappa_w*R))/(c2Sqr*j1(kappa_w*R)) #/ 5000
	


params = curve_fit(fit_anom, r, d)

# [a, b, c] = params[0]
[kappa_w] = params[0]

# print(r"a = ", a, "b = ", b, "c = ", c)
print(f"kappa_w = {kappa_w}")

# j10 = j1(0)
# print(f"j1(0) = {j10}")

print("min(r) = ", min(r), "max(r) = ", max(r))

# define a sequence of inputs between the smallest and largest known inputs
x_line = np.arange(0, R, 0.1) #np.arange(min(r), max(r)) #	
# calculate the output for the range
# y_line = fit_anom(x_line, a, b, c)


# kappa_w = 0.08 #1e-3
# y_line = fit_anom(x_line, kappa_w) #fit_anom(x_line, 0.05, 1e-5)#




#-----  fit elastic solution -----#
# def fit_elastic(x, al):
	# return -al*x*(x*x - R*R)/(8.0*c2*c2*c2*c2)

# params = curve_fit(fit_elastic, r, d)

# x_line_e = np.arange(0, R, 0.1) #np.arange(min(r), max(r))#
# y_line_e = fit_elastic(x_line_e, a)
#---------------------------------#



# ----- elastic_anomalous_difference -----#
# len_list = len(y_line)
#scale = []
# y_line_es = [] # scaled quasielastic solution
# mean_value = 0
# for i in range(1, len_list-1):
	# scale_factor = y_line[i] / y_line_e[i]
	# y_line_es.append( scale_factor *  y_line_e[i] )
	# d_s.append( scale_factor * d[i] )
	# mean_value += scale_factor

# x_line_es = x_line_e[1:len_list-1]

# mean_value = mean_value / (len_list-2)

# print( f'mean value of scale factor = {mean_value}' )


scale_factor = 10
d_s = [i * scale_factor for i in d] # scaled simulation data
# y_line_es = [i * scale_factor for i in y_line] # scaled quasielastic solution


# print(f'len(x_line) = {len(x_line)}')
# print(f'len(x_line_e) = {len(x_line_e)}')


# draw plots
fig, axs = plt.subplots(figsize=(11, 7))

# plt.rc('text', usetex=True)

# ttext = f"Na = {Na}, " + r"$\phi = $" + f"{phi},   P = {press},   " + r"$K_{n} = 2000$" + "\n" \
# 		r"$\underline{anomalous\,const:}$" + "\n" \
# 		r"$\widetilde{\kappa} = $" + f"{kappa_w:.5}," + r"$c_{2} = $" + f"{c2},   " \
# 		r"$\underline{elastic\,const:}$" + "\n" \
# 		f"a = {a:.5}\n" \

text2 = f'scale factor = {scale_factor}\n' + r"$\widetilde{\kappa} = $" + f"{kappa_w:.5}"
# axs.text(25, 1, text2, fontsize=16)

# axs.plot( x_line_e, y_line_e, lw=4, ls='-', color='red')#, label = 'quasielastic')#, a = ' + f'{a:.7f}')
# axs.plot( x_line_e, y_line_es, lw=7, ls='--', label = "quasielastic scaled")

# kappa_w = 0.01
# while kappa_w <= 0.1:
# 	y_line = fit_anom(x_line, kappa_w)
# 	axs.plot( x_line, y_line, lw=3, ls='-', label = r"$\kappa = $" + f"{kappa_w}")
# 	kappa_w += 0.01


# kappa_w = [0.0001, 0.001, 0.01, 0.02, 0.03]
# colors_kappa_w = ['green', 'seagreen', 'mediumspringgreen', 'lightseagreen', 'darkcyan']

# for i in range(len(kappa_w)):

# 	y_line = fit_anom(x_line, kappa_w[i])
# 	anom_text = "anomalous, " + r"$\kappa = $" + f"{kappa_w[i]}"
# 	axs.plot( x_line, y_line, lw=2, ls='-', color=colors_kappa_w[i], label=anom_text )


kappa_w = 0.33

y_line = fit_anom(x_line, kappa_w)
# anom_text = "anomalous, " + r"$\kappa = $" + f"{kappa_w}"
axs.plot( x_line, y_line, lw=4, ls='-', color='green')#, label=anom_text )



# plt_text = f"Na = {Na}\n" + r"$\phi = $" + f"{phi}\nP = {press}"
# axs.text(min(r), max(d)-0.15*(max(d)-min(d)), plt_text, fontsize=16)


# axs.plot( x_line[::-1], y_line, lw=3, ls='-', label = "anomalous reversed") # reversed x coordinates
axs.plot( r, d, lw=2, marker='o', ls="none", markersize=16, color='black', markerfacecolor=(0, 0, 0, 0.55))#, label = "simulation")
# axs.plot( r, d_s, lw=2, marker='o', ls="-", label = "simulation scaled")

axs.axhline( y=0, color='grey', linestyle='--' )


plt.xlabel('$r$', fontsize=28, loc='right')
plt.ylabel('$D$', fontsize=28, loc='top', rotation=0)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# axs.legend(fontsize=24, loc='upper center', bbox_to_anchor=(0.5, 1.15))

# plt.title(r'$\alpha = $' + f'{alpha}' + r'$,  c_2 = $' + f'{c2}', fontsize=22)
# plt.title(r"$\widetilde{K} = $" + f"{a:.5f}", fontsize=24)
plt.title(r"$\widetilde{\kappa} = $" + f"{kappa_w}", fontsize=24)


# DIR = 'results/Kn=' + str(Kn) + '_Na=' + str(Na) + '_P=' + str(press)
DIR = './summary/22-12-13_0.842/anomalous/zoomed_out' #'summary/images'
# name_save = 'fit_quasiel_anom_Na=' + str(Na) + '_phi=' + str(phi) + '_P=' + str(press) + '_c2=' + str(c2) + '_damp=' + str(damp) #'fit_elastic_anomalous_Na=' + str(Na) + '_Kn=' + str(Kn) + '_phi=' + str(phi) + '_P=' + str(press)
# name_save = f'displ_phi{phi}_Kn' + Knstr + f'_alpha{alpha}_c2{c2}'

# name_save = f'quasiel_phi{phi}_Kn' + Knstr + f'_alpha{alpha}_c2{c2}'
name_save = f'anomal_phi{phi}_Kn' + Knstr + f'_alpha{alpha}_c2{c2}_kappa{kappa_w}'

plt.savefig(DIR + '/' + name_save + '.jpg', dpi=100)


plt.show()
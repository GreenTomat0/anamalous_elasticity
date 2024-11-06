import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import j1


# press = 0.00081
# phi = 0.842
R = 29.68
# Na = 2000
# Kn = 20
# Knstr = '20'
# alpha = 0.3
# c2 = 1.8
K_w = 8e-4
# a_test = a
# damp = 0.1
# Knwall = '5Kn'
# nu = 0.3
# K = 0.1



# DIR = 'results/fixed_center/Kn' + Knstr + '/Knwall' + Knwall + '/Na_' + str(Na) + '-phi_' + str(phi) + '-Kn_' + Knstr + '-alpha_' + str(alpha) + '-c2_' + str(c2)
# filename = 'displ_vs_r_Na=' + str(Na) + '_alpha=' + str(alpha) + '_Kn=' + str(Kn) + '_P=' + str(press) +'.dat'

# radius & displacements
# r = []
# d = []

# path = DIR + '/' + filename

# with open(path) as f:
# 	next(f)	
# 	for line in f:
# 		r.append(float(line.split()[1]))
# 		d.append(float(line.split()[2]))
# f.close()



def fit_elastic(x, K_w, c2):
	return -K_w*x*(x*x - R*R)/(8.0*c2*c2*c2*c2)

# params = curve_fit(fit_elastic, r, d)

# [a] = params[0]

# x_line_e = np.arange(0, R, 0.1) #np.arange(min(r), max(r))#
# y_line_e = fit_elastic(x_line_e, a)


def fit_anom(x, K_w, kappa_w, c2):
	c2Sqr = c2*c2
	# j1 is the Bessel function of kind one, order 1
	return ( 1 - c2Sqr - K_w/(kappa_w*kappa_w*c2Sqr) )*(x*j1(kappa_w*R) - R*j1(kappa_w*x))/(c2Sqr*j1(kappa_w*R))
	# return ( 1 - c2Sqr - a/(kappa_w*kappa_w*c2Sqr) )*(R*j1(kappa_w*x) - x*j1(kappa_w*R))/(c2Sqr*j1(kappa_w*R)) #/ 5000
	


# params = curve_fit(fit_anom, r, d)

# [a, b, c] = params[0]
# [kappa_w] = params[0]

# print(r"a = ", a, "b = ", b, "c = ", c)
# print(f"kappa_w = {kappa_w}")

# j10 = j1(0)
# print(f"j1(0) = {j10}")

# print("min(r) = ", min(r), "max(r) = ", max(r))

# define a sequence of inputs between the smallest and largest known inputs
x = np.arange(0, R, 0.1) #np.arange(min(r), max(r)) #	
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


# scale_factor = 10
# d_s = [i * scale_factor for i in d] # scaled simulation data
# y_line_es = [i * scale_factor for i in y_line] # scaled quasielastic solution


# print(f'len(x_line) = {len(x_line)}')
# print(f'len(x_line_e) = {len(x_line_e)}')


# draw plots
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# plt.rc('text', usetex=True)

# ttext = f"Na = {Na}, " + r"$\phi = $" + f"{phi},   P = {press},   " + r"$K_{n} = 2000$" + "\n" \
# 		r"$\underline{anomalous\,const:}$" + "\n" \
# 		r"$\widetilde{\kappa} = $" + f"{kappa_w:.5}," + r"$c_{2} = $" + f"{c2},   " \
# 		r"$\underline{elastic\,const:}$" + "\n" \
# 		f"a = {a:.5}\n" \

# text2 = f'scale factor = {scale_factor}\n' + r"$\widetilde{\kappa} = $" + f"{kappa_w:.5}"
# axs.text(25, 1, text2, fontsize=16)

# axs.plot( x_line_e, y_line_e, lw=3, ls='-', color="red", label = 'quasielastic, a = ' + f'{a:.7f}')
# axs.plot( x_line_e, y_line_es, lw=7, ls='--', label = "quasielastic scaled")

# kappa_w = 0.01
# while kappa_w <= 0.1:
# 	y_line = fit_anom(x_line, kappa_w)
# 	axs.plot( x_line, y_line, lw=3, ls='-', label = r"$\kappa = $" + f"{kappa_w}")
# 	kappa_w += 0.01


# kappa_w = 0.2

clr = ['blue', 'orange', 'green']


#--- left subplot ---#
c2 = [1.8, 1.98]
kappa_w = 8e-3

for i in range(len(c2)):
	#--- anomoulous ---#
	y = fit_anom(x, K_w, kappa_w, c2[i])
	text = r'$c_2 = $' + f'{c2[i]}'
	axs[0].plot( x, y, lw=3, ls='-', color=clr[i], label=text )

#--- quasielastic ---#
y = fit_elastic(x, K_w, c2[0])
text = 'quasielastic, ' + r'$c_2 = $' + f'{c2[0]}'
axs[0].plot( x, y, lw=3, ls='-', color=clr[-1], label=text )

handles, labels = axs[0].get_legend_handles_labels()
order = [0,2,1]
axs[0].legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc='lower center', bbox_to_anchor=(0.5, -0.3), fancybox=True, ncol=2, fontsize=16)



#--- right subplot ---#
kappa_w = [0.1, 0.2, 0.3]
c2 = 1.8

for i in range(len(kappa_w)):
	y = fit_anom(x, K_w, kappa_w[i], c2)
	text = r'$\tilde \kappa = $' + f'{kappa_w[i]}'
	axs[1].plot( x, y, lw=3, ls='-', color=clr[i], label=text )

axs[1].legend(loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=3, fancybox=True, fontsize=16)


#--- figures decoration ---#
for i in range(2):
	axs[i].tick_params(axis='both', which='major', labelsize=16)
	axs[i].axhline( y=0, color='gray', linestyle='--' )

# axs[0].legend(loc='lower center', bbox_to_anchor=(0.5, -0.1), ncol=2, fancybox=True, fontsize=16)

axs[0].set_ylabel('D(r)', fontsize=24)
# fig.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), fancybox=True, ncol=4, fontsize=20)
fig.tight_layout()

# plt.title(r'$\alpha = $' + f'{alpha}' + r'$,  c_2 = $' + f'{c2}', fontsize=22)


# DIR = 'results/Kn=' + str(Kn) + '_Na=' + str(Na) + '_P=' + str(press)
# DIR = './summary/22-12-13_0.842/Knwall' + Knwall + '/' #'summary/images'
# name_save = 'fit_quasiel_anom_Na=' + str(Na) + '_phi=' + str(phi) + '_P=' + str(press) + '_c2=' + str(c2) + '_damp=' + str(damp) #'fit_elastic_anomalous_Na=' + str(Na) + '_Kn=' + str(Kn) + '_phi=' + str(phi) + '_P=' + str(press)

# plt.savefig(DIR + '/' + name_save + '.jpg', dpi=100)

folder_save = 'summary/additional_material/'
name_save = 'check_analytical_func' # name_save = 'infl_func_alpha_' + str(alpha) + '_diff_c2'

# fig.savefig(folder_save + '/' + name_save + '.jpg', dpi=100, bbox_inches='tight')


plt.show()
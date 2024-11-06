import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import sys


sys.path.insert(0, '/modules/') # adding 'modules' directory to the system path

from modules import fitting



phi = 0.836
R = 29.75
alpha = [0.1, 0.2, 0.3]
Kn = 20000
c2 = 1.95


if Kn > 2000:
	Kn_to_str = str(Kn)
	Kn_0_len = len(Kn_to_str) - 1

	Kn_str = '2e' + str(Kn_0_len)
else:
	Kn_str = str(Kn)



folder_name = f'sample_data/phi={phi}'

r = []
d = [] # radial displacement

#--- draw plot ---#
fig, axs = plt.subplots(2, 3, figsize=(15, 6))


img_dir = f'sample_data/phi={phi}/vector_field/'



for indx in range( len(alpha) ):
	#--- top raw, different alpha ---#
	filename = f'displ_vs_r_phi={phi}_Kn={Kn}_alpha={alpha[indx]}_c2={c2}.dat'
	
	with open(folder_name + '/' + filename) as f:
		next(f)
		for line in f:
			r.append(float(line.split()[1]))
			d.append(float(line.split()[2]))
	f.close()

	[x_el_approx, y_el_approx, a] = fitting.fit_quasielastic(r, d, R, c2)


	axs[0, indx].plot( r, d, linestyle='none', color='black', marker='o', markerfacecolor=(0, 0, 0, 0.5), markersize=8, label = 'numerical data')
	axs[0, indx].plot( x_el_approx, y_el_approx, lw=2, ls='-', color='red', label = 'analytical data')

	axs[0, indx].set_title(r'$\alpha = $' + f'{alpha[indx]}', fontsize=24) 

	r.clear()
	d.clear()

	#--- bottom raw, vector fields ---#
	img = plt.imread(img_dir + f'vector_field_phi{phi}_Kn{Kn_str}_alpha{alpha[indx]}_c2_{c2}.png')
	axs[1, indx].imshow(img)

	axs[1, indx].set_xticks([])
	axs[1, indx].set_yticks([])

axs[0, 0].set_ylabel(r'$D(r)$', fontsize=24)

axs[0, 0].legend(loc='lower center', bbox_to_anchor=(1.74, -1.5), ncol=2, fancybox=True, fontsize=16)



folder_save = 'summary/additional_material/'
name_save = f'sample_data_displ_phi{phi}_diff_alpha_vector_field' # name_save = 'infl_func_alpha_' + str(alpha) + '_diff_c2'

# fig.savefig(folder_save + '/' + name_save + '.jpg', dpi=100, bbox_inches='tight')


plt.show()
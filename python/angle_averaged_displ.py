import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d



phi = 0.836
R = 29.75
Kn = 20000

alpha = [0.1, 0.2, 0.3]
c2 = [1.98, 1.9, 1.8]


folder_name = f'sample_data/phi={phi}'

r = []
rad = [] # radial displacement
az = [] # azimuthal displacement

#--- draw plot ---#
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(11, 8))

clrs = ['blue', 'orange', 'green']
markers = ['o', 's', 'v'] 


#--- left figure, alpha = 0.1 ---#
for indx in range( len(c2) ):

	filename = f'displ_vs_r_phi={phi}_Kn={Kn}_alpha={alpha[0]}_c2={c2[indx]}.dat'

	
	with open(folder_name + '/' + filename) as f:
		next(f)
		for line in f:
			r.append(float(line.split()[1]))
			rad.append(float(line.split()[2]))
			az.append(float(line.split()[3]))
	f.close()


	text = r'$c_2 = $' + f'{c2[indx]}'
	axs[0, 0].plot( r, rad, linestyle='-', color=clrs[indx], marker=markers[indx], markersize=10, label = text)
	axs[1, 0].plot( r, az, linestyle='-', color=clrs[indx], marker=markers[indx], markersize=10)#, label = text)

	r.clear()
	rad.clear()
	az.clear()



# #--- right figure, alpha = 0.3 ---#
for indx in range( len(c2) - 1 ):

	filename = f'displ_vs_r_phi={phi}_Kn={Kn}_alpha={alpha[2]}_c2={c2[indx + 1]}.dat'

	
	with open(folder_name + '/' + filename) as f:
		next(f)
		for line in f:
			r.append(float(line.split()[1]))
			rad.append(float(line.split()[2]))
			az.append(float(line.split()[3]))
	f.close()
	

	# text = r'$c_2 = $' + f'{c2[indx]}'
	axs[0, 1].plot( r, rad, linestyle='-', color=clrs[indx+1], marker=markers[indx+1], markersize=10)
	axs[1, 1].plot( r, az, linestyle='-', color=clrs[indx+1], marker=markers[indx+1], markersize=10)

	r.clear()
	rad.clear()
	az.clear()



for i in range(2):
	for j in range(2):
		axs[i, j].tick_params(axis='both', which='major', labelsize=16)
		axs[i, j].axhline( y=0, color='gray', linestyle='--' )

axs[0, 0].set_ylabel(r'$D(r)$', fontsize=24)
axs[1, 0].set_ylabel(r'$D_{\perp}(r)$', fontsize=24)

axs[0, 0].set_title(r'$\alpha = $' + f'{alpha[0]}', fontsize=24)
axs[0, 1].set_title(r'$\alpha = $' + f'{alpha[2]}', fontsize=24)

fig.legend(loc='lower center', bbox_to_anchor=(0.5, -0.05), fancybox=True, ncol=3, fontsize=20)

# fig.tight_layout()







folder_save = 'summary/additional_material/'
name_save = f'sample_data_displ_phi{phi}_Kn{Kn}' # name_save = 'infl_func_alpha_' + str(alpha) + '_diff_c2'

fig.savefig(folder_save + '/' + name_save + '.jpg', dpi=100, bbox_inches='tight')


plt.show()
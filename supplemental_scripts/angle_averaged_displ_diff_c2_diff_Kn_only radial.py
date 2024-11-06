import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d



phi = 0.836
R = 29.75
alpha = 0.2
Kn = [20, 200, 2000, 20000]
c2 = [1.98, 1.9, 1.8]


folder_name = f'sample_data/phi={phi}'

r = []
rad = [] # radial displacement

#--- draw plot ---#
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

clrs = ['blue', 'orange', 'green', 'red']
markers = ['o', 's', 'v', 'x'] 

l = [None]*len(c2)
plot_lines = []

#--- left figure, different c2, Kn = 2*10^4 ---#
for indx in range( len(c2) ):

	filename = f'displ_vs_r_phi={phi}_Kn={Kn[3]}_alpha={alpha}_c2={c2[indx]}.dat'
	
	with open(folder_name + '/' + filename) as f:
		next(f)
		for line in f:
			r.append(float(line.split()[1]))
			rad.append(float(line.split()[2]))
	f.close()


	text_c2 = r'$c_2 = $' + f'{c2[indx]}'
	axs[0].plot( r, rad, linestyle='-', color=clrs[indx], marker=markers[indx], markersize=10, label = text_c2)

	r.clear()
	rad.clear()

axs[0].legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=3, fancybox=True, fontsize=16)




l2 = [None]*len(Kn)
plot_lines2 = []

# #--- right figure, different Kn, c2 = 1.9 ---#
for indx in range( len(Kn) ):

	filename = f'displ_vs_r_phi={phi}_Kn={Kn[indx]}_alpha={alpha}_c2={c2[1]}.dat'
	
	with open(folder_name + '/' + filename) as f:
		next(f)
		for line in f:
			r.append(float(line.split()[1]))
			rad.append(float(line.split()[2]))
	f.close()
	

	text_Kn = r'$K_n = $' + f'{Kn[indx]}'
	axs[1].plot( r, rad, linestyle='-', color=clrs[indx], marker=markers[indx], markersize=10, label = text_Kn)

	r.clear()
	rad.clear()

axs[1].legend(loc='lower center', bbox_to_anchor=(0.5, -0.35), ncol=2, fancybox=True, fontsize=16)


for i in range(2):
	axs[i].tick_params(axis='both', which='major', labelsize=16)
	axs[i].axhline( y=0, color='gray', linestyle='--' )

axs[0].set_ylabel(r'$D(r)$', fontsize=24)

axs[0].set_title(r'$\alpha = $' + f'{alpha}, ' + r'$K_n = $' + f'{Kn[3]}', fontsize=24)
axs[1].set_title(r'$\alpha = $' + f'{alpha}, ' + r'$c_2 = $' + f'{c2[1]}', fontsize=24)



# legend1 = fig.legend(handles=plot_lines[0], loc='lower center', bbox_to_anchor=(0.3, -0.1), fancybox=True, ncol=2, fontsize=18)
# fig.add_artist(legend1)

# fig.legend(handles=plot_lines2[0], loc='lower center', bbox_to_anchor=(0.725, -0.1), fancybox=True, ncol=2, fontsize=18)
fig.tight_layout()







folder_save = 'summary/additional_material/'
name_save = f'sample_data_displ_phi{phi}_diff_c2_diff_Kn_only_radial' # name_save = 'infl_func_alpha_' + str(alpha) + '_diff_c2'

fig.savefig(folder_save + '/' + name_save + '.jpg', dpi=100, bbox_inches='tight')


plt.show()
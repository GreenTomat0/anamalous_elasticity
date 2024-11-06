import numpy as np
import math
import matplotlib.pyplot as plt



L = 29.68 #66.17 #66.25 # # initial radius
phi = 0.84 #
x = np.arange(0, L, 1) # y = 0  - we check only for points that are lies on positive x-axis
# c2 = 1.9 #1.98 #
# alpha = 0.1



r_sqr = [i*i for i in x]
r = [i for i in x]

#-- this is for y = 0


def infl_func(alpha, cc2):
	
	k0 = alpha / L
	
	func = []
	for elem in r_sqr:
		deter = k0*k0*elem + cc2*cc2
		func.append( 4.0*cc2*cc2 / (deter*deter) )
	

	return func
		

# draw plot
fig, axs = plt.subplots(1, 3, figsize=(15, 4), sharey=True) #figsize=(11, 7)

# for al in [0.1, 0.2, 0.3, 0.5]:
# 	label = (r"$\alpha$ = " + str(al))
# 	plt.plot(r, infl_func(al, c2, L, r_sqr), label=label)

alpha = [0.1, 0.2, 0.3]
for c2 in [1.98, 1.95, 1.9, 1.8]: #
	label = (r"$c_2$ = " + str(c2))
	axs[0].plot(r, infl_func(alpha[0], c2), label=label)
	axs[1].plot(r, infl_func(alpha[1], c2))
	axs[2].plot(r, infl_func(alpha[2], c2))

	



# axs[0].get_shared_x_axes().join(axs[0], *axs[1:])
# axs[0].set_xticklabels('r')

# plt.title(r'$\alpha = $' + f'{alpha}', fontsize=22)
# axs[0].xlabel('r', fontsize=24)
axs[0].set_ylabel('F(r)', fontsize=24)
# plt.ylabel('Infl func', fontsize=20)
# fig.set_xticks(fontsize=14)
# axs.set_yticks(fontsize=14)

# fig.legend(fontsize=16, loc='best')

for i in range(3):
	axs[i].set_title(r'$\alpha = $' + f'{alpha[i]}', fontsize=24)
	axs[i].tick_params(axis='both', which='major', labelsize=16)

	axs[i].axhline( y=1, color='gray', linestyle='--' )


fig.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), fancybox=True, ncol=4, fontsize=20)
fig.tight_layout()


folder_save = 'summary/additional_material/'
name_save = 'infl_func_alpha_c2' # name_save = 'infl_func_alpha_' + str(alpha) + '_diff_c2'

fig.savefig(folder_save + '/' + name_save + '.jpg', dpi=100, bbox_inches='tight')

plt.show()



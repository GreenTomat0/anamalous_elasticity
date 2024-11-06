import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import cv2
import os.path
from os import path



phi_values = [0.836, 0.838, 0.84, 0.842, 0.844]
Kn_values = [2*(10**i) for i in range(1, 7)] #[20, 200, 2000, 2e4, 2e5, 2e6]

phi = []
Kn = []

j = 0
while j < len(phi_values):
	for i in range(len(Kn_values)):
		phi.append(phi_values[j])
		Kn.append(Kn_values[i])
	j += 1


# convert lists to arrays
phi = np.array(phi)
Kn = np.array(Kn)





# fig = plt.subplots()#figsize=(13, 7))
fig = plt.figure(figsize=(12, 7))#(16, 8)

# subfigs = fig.subfigures(1, 2, wspace=0.07)

# axsRight = subfigs[1].subplots(2, 2)


# sub1 = plt.subplot(1, 2, 1) # (nrows, ncols, plot_number)
# create 1x2 subfigures
# fig = plt.figure(constrained_layout=True, figsize=(12, 5))
# (subfig_l, subfig_r) = fig.subfigures(nrows=1, ncols=2, wspace=0.07)

outer = mpl.gridspec.GridSpec(1, 2, wspace=0.1, hspace=0.05)

inner_rows = 4
inner_cols = 3
widths = [1, 2]
inner = mpl.gridspec.GridSpecFromSubplotSpec(inner_rows, inner_cols, subplot_spec=outer[1], wspace=0.02, hspace=0.02)#, width_ratios=widths)


ax_left = plt.Subplot(fig, outer[0])
fig.add_subplot(ax_left)

ax_left.scatter(phi, Kn, marker='o', s=150, color='darkblue', edgecolor='red', picker=True, pickradius=5)
ax_left.set_yscale('log')
ax_left.set_yticks(Kn)
ax_left.get_yaxis().set_major_formatter(mpl.ticker.StrMethodFormatter("{x:,g}"))
ax_left.set_xlim(min(phi) - 0.001, max(phi) + 0.001)
ax_left.set_xlabel(r'$\phi$', fontsize=20)
ax_left.set_ylabel(r'$K_n$', fontsize=20)
ax_left.tick_params(axis='both', which='major', labelsize=14)
ax_left.grid()


ax_right = plt.Subplot(fig, outer[1]) #outer[0, 1:]
fig.add_subplot(ax_right)
ax_right.set_xticks([])
ax_right.set_yticks([])

k = -1
for i in range(0, inner_rows):
	for j in range(0, inner_cols):
		k += 1
		globals()[f'ax_right_{i}{j}'] = plt.Subplot(fig, inner[k])
		globals()[f'ax_right_{i}{j}'].set_xticks([])
		globals()[f'ax_right_{i}{j}'].set_yticks([])
		fig.add_subplot(globals()[f'ax_right_{i}{j}'])



default_image = 'images_gallery/default/default.jpg'

for i in range(0, inner_rows):
    	for j in range(0, inner_cols):
    		# globals()[f'ax_right_{i}{j}'].clear()
    		
    		im = plt.imread(default_image)
    		
    		globals()[f'ax_right_{i}{j}'].imshow(im)
    		globals()[f'ax_right_{i}{j}'].set_xticks([])
    		globals()[f'ax_right_{i}{j}'].set_yticks([])
		





# c2 = {0: 1.98, 1: 1.95, 2: 1.9, 3: 1.8}

# alpha = {0: 0.1, 1: 0.2, 2: 0.3}

alpha = [0.1, 0.2, 0.3]
c2 = [1.98, 1.95, 1.9, 1,8]


def onpick(event):
    ind = event.ind
    # print('onclick scatter:', ind, phi[ind], Kn[ind])

    for i in range(0, inner_rows):
    	for j in range(0, inner_cols):
    		# globals()[f'ax_right_{i}{j}'].clear()
    		# bkgr_color = tuple(np.random.random(size=3))
    		
    		image_name = f'images_gallery/phi={phi[ind][0]}/displ_phi={phi[ind][0]}_Kn={Kn[ind][0]}_alpha={alpha[j]}_c2={c2[i]}.jpg'
    		# print(image_name)
    		
    		# print(path.exists(image_name))
    		if path.exists(image_name):
	    		im = plt.imread(image_name)
	    	else:
	    		im = plt.imread(default_image)
	    	
	    	globals()[f'ax_right_{i}{j}'].imshow(im)
	    	
	    	globals()[f'ax_right_{i}{j}'].set_xticks([])
	    	globals()[f'ax_right_{i}{j}'].set_yticks([])

    plt.draw()

    # ax_right.canvas.draw_idle()
    

props = dict(facecolor='red') #(1.0, 0.47, 0.42)


# def onclick_select(event):

#     for i in range(0, inner_rows):
#         for j in range(0, inner_cols):

#             if event.inaxes == globals()[f'ax_right_{i}{j}']:
#                 event.inaxes.cla()
#                 event.inaxes.set_facecolor((1.0, 0.47, 0.42))

#                 event.inaxes.update(props)

#                 # event.inaxes.update(props)


    
    # if event.inaxes == ax_left:
    #     print ("ax_left")
    # elif event.inaxes == ax_right:
    #     print (f'inner')









fig.canvas.mpl_connect('pick_event', onpick)

# fig.canvas.mpl_connect('button_press_event', onclick_select)

# fig.canvas.mpl_connect('button_press_event', on_press)

# ax_left.canvas.mpl_connect('pick_event', onpick)


# mng = plt.get_current_fig_manager()
# mng.full_screen_toggle()


plt.show()

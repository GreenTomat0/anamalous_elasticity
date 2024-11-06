import numpy as np
import math
import matplotlib.pyplot as plt


CurvRad = [1.001, 1.01, 1.05, 1.1, 1.5, 10]
RadStart = 104.5

x = 1
y = 1

Func = [0]*len(CurvRad)

for i in range(len(CurvRad)):
	Deter = 4*RadStart*RadStart*(CurvRad[i]*CurvRad[i] - 1.0)#4*(CurvRad[i]*CurvRad[i] - RadStart*RadStart)
	Func[i] = np.sqrt( 2*CurvRad[i]*np.sqrt(Deter) / (x*x + y*y + Deter) )
	# print(Deter)


print(CurvRad)
print(Func)

		

# # draw plot
# fig, axs = plt.subplots(figsize=(11, 7))

# plt.xlabel('$CurvRad$', fontsize=20)
# plt.ylabel('$Func$', fontsize=20)
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)
# axs.legend(fontsize=16, loc='best')

# # interpolation
# # label_interp = "interpolation"
# # r_interp = np.linspace(r[0], r[-1], num=10000, endpoint=True)
# # d_interp = interp1d(r, disp_list, kind='cubic')
# # axs.plot(r_interp, d_interp(r_interp), lw=4, color="darkmagenta", label=label_interp)


# folder_save = 'results'
# name_save = 'Na=' + str(Na) + '_phi='+str(phi)+'_Kn='+str(Kn)+'_P='+str(press)

# plt.savefig(folder_save + '/' + name_save + '.pdf')

# plt.show()



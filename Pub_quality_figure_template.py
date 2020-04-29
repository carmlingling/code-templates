import matplotlib
matplotlib.rc('text', usetex = True)
import matplotlib.pyplot as plt
import numpy as np

data_x = np.linspace(0,15)
data_y = np.sin(data_x)


figure = plt.figure(1) #Makes a matplotlib figure, the 1 indicates the plot number, plotting more figures at once requires changing that number

figure.subplots_adjust(top=0.96, bottom=0.2, left=0.16, right=0.96)
axes = figure.add_subplot(111) # This allows for a subplot to be generated. More

axes.plot(data_x, data_y,'*', color = 'k', label = r'$\textrm{sin}\left(x\right)$')
axes.set_xlabel(r'$X \textrm{data}$', fontsize = 18)
axes.set_ylabel(r'$Y \textrm{data}$', fontsize = 18)
axes.tick_params(labelsize = 20)

axes.legend(loc = 3, fontsize = 16, frameon = False)
plt.show()

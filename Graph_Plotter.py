import matplotlib.plotly as plt
import numpy as np

#Generating data
x = np.linspace (0.1,10,400)
y = 1/x

#Plotting

plt.plot (x,y)
plt.xlabel ('x')
plt.ylable ('y')
plt.title ('Graph of y = 1/x ')
plt.show()

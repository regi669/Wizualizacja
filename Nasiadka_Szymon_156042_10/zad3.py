import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,30.1,0.1)
ys= np.sin(x)
yc= np.cos(x)

plt.plot(x,ys,label='sin(x)')
plt.plot(x,yc,label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
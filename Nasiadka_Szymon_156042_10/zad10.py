import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,30.1,0.1)
ys= np.sin(x)
yc= np.cos(x)

fig, ax = plt.subplots()
ax.plot(x,ys,label='sin(x)')
ax.plot(x,yc,label='cos(x)')
ax.annotate('sin(x)=0',
            xy=(0, 0), xycoords='data',
            xytext=(0,-1), textcoords='data',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.show()

fig, ax = plt.subplots()
x= range(1,21)
y= [1/y for y in x]
line, =ax.plot(x,y, label='f(2)=1/x')
ax.axis([1, len(x), 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks(np.arange(0,21,1))
plt.yticks(np.arange(0,1.1,0.1))
ax.annotate('f(2)=0.5',
            xy=(2, 0.5), xycoords='data',
            xytext=(5,0.8), textcoords='data',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='left', verticalalignment='bottom')
plt.legend()
plt.show()
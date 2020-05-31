
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
for x in range(0, 2):
    ax1 = fig.add_subplot(1, 2, x+1, projection = "3d")
    if(x==1):
        X = np.arange(- 5 , 5 , 0.10 )
        Y = np.arange(- 5 , 5 , 0.10 )
    else:
        X = np.arange(- 5 , 5 , 0.25 )
        Y = np.arange(- 5 , 5 , 0.25 )
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X** 2 + Y** 2 )
    Z = np.sin(R)
    if(x==1):
        surf = ax1.plot_surface(X, Y, Z, cmap =cm.binary,
        linewidth = 0 , antialiased = True )
    else:
        surf = ax1.plot_surface(X, Y, Z, cmap =cm.coolwarm,
        linewidth = 0 , antialiased = False )
    ax1.set_zlim(- 1.01 , 1.01 )
    ax1.zaxis.set_major_locator(LinearLocator( 10 ))
    ax1.zaxis.set_major_formatter(FormatStrFormatter( "%.02f" ))
    fig.colorbar(surf, shrink = 0.5 , aspect = 5 )
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.set_zlabel("Z")
    if(x==1):
        plt.title("Wykres po wprowadzonych zmianach")
    else:
        plt.title("Pierwotny wykres")
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

def randrange(n, vmin, vmax):
    """
    Funkcja wspomagająca może tworzyć macierz losowych liczb o
    kształcie(n, )
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

def losuj_kolor():
    kolory = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')
    return random.choice(kolory)

def losuj_marker():
    markery = ('.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', '*', 'h', 'H', '+', 'x', 'X', 'D', 'd', '|', '_')
    return random.choice(markery)

fig = plt.figure()
ax = fig.gca(projection = "3d")
n = 100

kolory = []
markery = []
for x in range(0, 5):
    while(1):
        cc = losuj_kolor()
        if(cc not in kolory):
            kolory.append(cc)
            break

    while(1):
        mm = losuj_marker()            
        if(mm not in markery):
            markery.append(mm)
            break

    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, random.randint(-100, 100), random.randint(-100, 100))
    ax.scatter(xs, ys, zs, c =kolory[x], marker =markery[x])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
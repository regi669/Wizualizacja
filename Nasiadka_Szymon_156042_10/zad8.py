import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dice(n):
    return [(np.random.randint(6)+1)+(np.random.randint(6)+1) for x in range(n)]

lista=dice(100)
plt.hist(lista, bins=10, facecolor="red", alpha=0.75)
plt.xlabel('Wartości')
plt.ylabel('Ilość rzutów o danej sumie')
plt.title('Histogram')
plt.grid(True)
plt.show()


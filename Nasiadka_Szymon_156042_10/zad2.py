import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = range(1,21)
y = [1/y for y in x]
plt.plot(x,y,'g:>',label='f(x)=1/x')
plt.axis([1, len(x), 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks(np.arange(0,21,2.5))
plt.title('Wykres funkcji f(x) dla x ϵ [1, 20]')
plt.legend()

plt.show()
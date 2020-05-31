import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"])

x = df["SepalLengthCm"]
y = df["SepalWidthCm"]

data = {"x": x,
        "y": y,
        "c": np.random.randint(0, 50, 150),
        "s": abs(x.subtract(y))}

plt.scatter('x', 'y', c='c', s='s', data=data)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()
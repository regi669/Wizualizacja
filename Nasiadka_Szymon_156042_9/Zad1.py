import pandas as pd
import matplotlib.pyplot as plt

f = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(f)

grupa = data.groupby(['Rok']).agg({'Liczba':['sum']})
grupa.plot()
plt.show()
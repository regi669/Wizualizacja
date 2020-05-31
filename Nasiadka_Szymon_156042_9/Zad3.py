import pandas as pd
import matplotlib.pyplot as plt

f = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(f)

high = data['Rok'].max()
grupa = data[data['Rok'] > high-5].groupby(['Plec']).agg({'Liczba':['sum']})
grupa.plot.pie(subplots = True,autopct='%.2f %%')
plt.show()
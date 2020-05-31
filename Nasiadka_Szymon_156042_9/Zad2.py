import pandas as pd
import matplotlib.pyplot as plt

f = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(f)

lista = []
for x in data['Imie']:
    if x[-1] == 'A':
        lista.append('kobieta')
    else:
        lista.append('mężczyzna')
data['Plec'] = lista

grupa = data.groupby(['Plec']).agg({'Liczba':['sum']})
grupa.plot.bar()
plt.show()

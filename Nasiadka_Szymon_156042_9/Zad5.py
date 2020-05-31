import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('zamowienia.csv', delimiter=';')
grupa = dane.groupby(['Sprzedawca']).agg({'idZamowienia':['sum']})

grupa.plot.bar()
plt.show()


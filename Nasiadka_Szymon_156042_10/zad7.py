import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df= pd.read_excel(pd.ExcelFile("imiona.xlsx"),"Arkusz1")
ch=df[df["Plec"]=='M'].groupby(['Rok']).sum()
dz=df[df["Plec"]=='K'].groupby(['Rok']).sum()

plt.bar(df.Rok.unique(),[ch.values[y][0] for y in range(len(ch.values))],color="red", label="M")
plt.bar(df.Rok.unique(),[dz.values[y][0] for y in range(len(dz.values))],color="green", label="K",  bottom=[ch.values[y][0] for y in range(len(ch.values))])
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.legend(loc='best')
plt.show()
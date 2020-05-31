import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df= pd.read_excel(pd.ExcelFile("imiona.xlsx"),"Arkusz1")
p=df.groupby(['Plec']).agg({"Liczba":["sum"]})
p2=df.groupby(['Rok']).agg({"Liczba":["sum"]})
ch=df[df["Plec"]=='M'].groupby(['Rok']).sum()
dz=df[df["Plec"]=='K'].groupby(['Rok']).sum()

plt.subplot(1,3,1)
plt.bar(['K','M'],[p.values[0][0],p.values[1][0]],color=['blue','cyan'])
plt.ylabel('Ilość urodzeń (mln)')
plt.xlabel('Płeć')
plt.subplot(1,3,2)
plt.plot(df.Rok.unique(),[ch.values[y][0] for y in range(len(ch.values))],"r", label="M")
plt.plot(df.Rok.unique(),[dz.values[y][0] for y in range(len(dz.values))],"g", label="K")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.legend()
plt.subplot(1,3,3)
plt.bar(df.Rok.unique(),[p2.values[y][0] for y in range(len(p2.values))],color="pink")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.show()
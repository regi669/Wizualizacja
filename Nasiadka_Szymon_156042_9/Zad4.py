import pandas as pd
import matplotlib.pyplot as plt


plik = pd.ExcelFile('imiona.xlsx')
dane = pd.read_excel(plik)


lista = []
for x in dane['Imie']:
    if x[-1] == 'A':
        lista.append('kobieta')
    else:
        lista.append('mężczyzna')
dane['Plec'] = lista




top = dane['Rok'].max()

dane2 = pd.read_csv('iris.data', sep=',', names=['sepal length in cm',  'sepal width in cm',  'petal length in cm', 'petal width in cm', 'class'])
grupa4 = dane2.copy()
grupa4['class'] = grupa4['class'].astype('|S')
grupa4.drop('petal length in cm', axis=1, inplace=True)
grupa4.drop('petal width in cm', axis=1, inplace=True)
lista1 = []
for x in grupa4['class']:
    if x == b'Iris-setosa':
        lista1.append('red')
    elif x == b'Iris-versicolor':
        lista1.append('blue')
    else:
        lista1.append('black')
grupa4['class'] = lista1

grupa4[grupa4['class']==b'Iris-setosa'].plot.scatter(x='sepal length in cm', y='sepal width in cm', c='black', label='Iris Setosa')
grupa4[grupa4['class']==b'Iris-versicolor'].plot.scatter(x='sepal length in cm', y='sepal width in cm', c='red', label='Iris Versicolour')
grupa4[grupa4['class']==b'Iris-virginica'].plot.scatter(x='sepal length in cm', y='sepal width in cm', c='blue', label='Iris Virginica')
grupa4.plot.scatter(x='sepal length in cm', y='sepal width in cm', c='class')

plt.show()


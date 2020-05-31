
from zadanie_2 import *
from lxml import html
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

newdf = df.sort_values(by=["Num Voters"], ascending=False)
top10 = newdf.head(10).reset_index()
print(top10)

tytuly = top10["Title"].tolist()
liczba_glosujacych = top10["Num Voters"].tolist()

plt.bar(tytuly, liczba_glosujacych)
plt.xticks(rotation=45)
plt.xlabel('Tytuł')
plt.ylabel('Liczba głosujących')
plt.title('Top10 gier z boardgamegeek')
plt.show()
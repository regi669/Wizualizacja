
from lxml import html
import requests
import pandas as pd

url = "https://boardgamegeek.com/browse/boardgame"
data = requests.get(url)

page = html.fromstring(data.text)
xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
table_div = page.get_element_by_id('collection')

table = table_div.xpath('./*[@class="table-responsive"]/table')[0]
labels = [label.strip() for label in table.xpath('.//th/text()')]

headers = [label for label in table.xpath('.//th')]
rows = [row for row in table.xpath('.//td')]
labels = []
labels2 = []

for header in headers:
    anchor = header.xpath('./a/text()')
    if len(anchor) > 0:
        labels.append(anchor[0].strip())
    else:
        labels.append(header.text.strip())

for row in rows:
    anchor = row.xpath('./div/a/text()')
    if len(anchor) > 0:
        labels2.append(anchor[0].strip())
    else:
        labels2.append(row.text.strip())

while('' in labels2) : 
    labels2.remove('') 

Title = []
Geek_Rating = []
Avg_Rating = []
Num_Voters = []
Board_Game_Rank = [x for x in range(1, 101)]

for x in range(0, 400, 4):
    Title.append(labels2[x])
    Geek_Rating.append(float(labels2[x+1]))
    Avg_Rating.append(float(labels2[x+2]))
    Num_Voters.append(int(labels2[x+3]))

d = {labels[0]: Board_Game_Rank, labels[2]: Title, labels[3]: Geek_Rating,
    labels[4]: Avg_Rating, labels[5]: Num_Voters}
df = pd.DataFrame(data=d)
# print(df)
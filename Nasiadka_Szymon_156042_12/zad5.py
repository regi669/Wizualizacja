
from bs4 import BeautifulSoup
import urllib3
import pandas as pd

def get_data_from_page():
    titles = []
    platforms = []
    relase_dates = []
    scores = []
    for tr in soup.find_all('tr'):
        for childtr in tr.find_all(class_="title"):
            for h3 in childtr.find_all("h3"):
                title = childtr.string.strip()
                titles.append(title)
        for childtr in tr.find_all(class_='platform'):
            for childtr in tr.find_all(class_='data'):
                platform = childtr.string.strip()
                platforms.append(platform)
        for childtr in tr.find_all(class_='clamp-details'):
            date = childtr.find_all("span")[2].get_text(strip=True)
            relase_dates.append(date)
        for childtr in tr.find_all(class_="metascore_w large game positive"):
            score = childtr.string
            scores.append(score)
            break
    return titles, platforms, relase_dates, scores

column_names = ["Tytuł", "Platforma", "Data wydania", "Ocena"]
final_df = pd.DataFrame(columns = column_names)
frames = []

for x in range(0, 10):
    url = "https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed&page=" + str(x)
    http = urllib3.PoolManager()
    page = http.request("GET", url)
    soup = BeautifulSoup(page.data, 'lxml')

    t, p, rd, s = get_data_from_page()

    d = {"Tytuł": t, "Platforma": p, "Data wydania": rd,
        "Ocena": s}
    df = pd.DataFrame(data=d)
    frames.append(df)
    
final_df = pd.concat(frames).reset_index(drop=True)
top_10_PC = final_df.loc[final_df["Platforma"]=="PC"].head(10)
print(top_10_PC.reset_index())
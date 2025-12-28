import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}
url = "https://en.wikipedia.org/wiki/World_Happiness_Report#2019_report"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

happy_data = []

for header in soup.find_all("h2", {"id": "International_rankings"}):
    table = header.find_next("table")
    if table is None:
        continue

    for tr in table.find_all("tr")[1:]:

        if tr.find("th"):
            continue
        tds = tr.find_all("td")

        if len(tds) == 0:
            continue

        # Extract each column
        row = [
            tds[0].text.strip(),   # Overall Rank
            tds[1].text.strip(),   # Country
            tds[2].text.strip(),   # Score
            tds[3].text.strip(),   # Log GDP
            tds[4].text.strip(),   # Social support
            tds[5].text.strip(),   # Healthy life expectancy
            tds[6].text.strip(),   # Freedom to make life choices
            tds[7].text.strip(),
            tds[8].text.strip(),


        ]

        # Append row normally (not nested)
        happy_data.append(row)

# Create dataframe column-wise
df = pd.DataFrame(happy_data, columns=[
    "Overall Rank", "Country", "Score",
    "Log GDP", "Social Support",
    "Healthy Life Expectancy", "Freedom To Make Life Choices", "Generosity", "Perceptions Of Corruption"])

print(df)

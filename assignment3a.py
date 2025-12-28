import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}
url = "https://simple.wikipedia.org/wiki/List_of_countries_by_continents"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

continents = ["Africa", "Asia", "Europe",
              "North America", "South America", "Oceania"]

country_data = []

for header in soup.find_all("h2"):
    continent = header.text.replace("[edit]", "").strip()

    # Check if this header starts with any continent name
    if any(continent.startswith(c) for c in continents):

        table = header.find_next("table")
        if table is None:
            continue

        for tr in table.find_all("tr")[1:]:
            tds = tr.find_all("td")

            if len(tds) == 0:
                continue

            country = tds[0].text.strip()
            country_data.append([continent.split()[0], country])

df = pd.DataFrame(country_data, columns=["continent", "country"])
print(df)

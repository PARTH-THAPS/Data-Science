import numpy as np
import array
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import plotly.express as px

# array.array('d',[1.5,2.8,0.2,3.1])

arr = np.array([1.5, 2.8, 0.2, 3.1])

print(type(arr))
print(f"Second Element of the Array {arr[1]}")

print(f"Second and third element of the Array {arr[1]}, {arr[2]}")
arr[0] = 23.0
print(f"Changed Array {arr}")
print(arr[arr > 2])
x_squared = arr * 2

print(f"Type Of {type(x_squared)}. {x_squared}")
arr = np.append(arr, 5.2)
print(arr)

list = [-5, 7, 8, "Error", 5]

for i in range(len(list)):
    print(f"Type Of Data Type {type(list[i])}")
    if list[i] == "Error":
        print(list[i])


list.append(3)
list.append(3)

for i in range(len(list)):
    print(f"Type Of Data Type {type(list[i])}")
    if list[i] == "Error":
        list[i] = 0


print(f"Print New List after The Operation. {list}")


medals = {}

print(type(medals))


medals = {
    "Germany": 36,
    "China": 100,
    "Usa": 112
}

medals["Italy"] = 40

medals.pop("Germany")
medals.update({"Usa": 113})
print(f"Medals Key {medals.keys()}")
print(f"Medals Values {medals.values()}")


matrix = [[2, 4, 3], [1, 5, 7]]

for row in matrix:
    print(row)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 5:
            matrix[i][j] = 0


data = {
    'Country': ['NOR', 'GER', 'CHN'],
    'Gold': [16, 12, 9],
    'Silver': [8, 10, 4],
    'Bronze': [13, 5, 2],
}


df = pd.DataFrame(data)
print(df)

print(df.iloc[[0, 2], [0, 2]])
print(df[df["Country"] == "CHN"])
print(df[df["Country"].isin(["GER", "NOR"])])
print(df[df["Gold"] > 10][["Country", "Gold"]])
print(df.sort_values(by="Bronze", ascending=False))

Olymics_medal = pd.read_csv("/Users/user/Downloads/Beijing1.csv", sep=';')
print(Olymics_medal)

Olymics_medal["Total"] = Olymics_medal["Gold"] + \
    Olymics_medal["Silver"]+Olymics_medal["Bronze"]


print(Olymics_medal)
Olymics_medal = Olymics_medal.sort_values(
    by=["Total", "Gold"], ascending=[False, False])

total_numbers_of_gold = Olymics_medal["Gold"].sum()

print(total_numbers_of_gold)


headers = {"User-Agent": "Mozilla/5.0"}
url = "https://en.wikipedia.org/wiki/World_Happiness_Report#2019_report"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

happy_data = []

for header in soup.find_all("h2", {"id": "International_rankings"}):
    table = header.find_next("table")
    if table is None:
        continue

    for tr in table.find_all("tr"):
        # Skip header rows
        if tr.find("th"):
            continue

        tds = tr.find_all("td")
        if len(tds) < 9:
            continue

        row = [
            tds[0].text.strip(),   # Overall Rank
            tds[1].text.strip(),   # Country
            tds[2].text.strip(),   # Score
            tds[3].text.strip(),   # Log GDP
            tds[4].text.strip(),   # Social support
            tds[5].text.strip(),   # Healthy life expectancy
            tds[6].text.strip(),   # Freedom to make life choices
            tds[7].text.strip(),   # Generosity
            tds[8].text.strip()    # Perceptions of corruption
        ]

        happy_data.append(row)
HappyDataPd = pd.DataFrame(happy_data, columns=["Overall Rank", "Country", "Score",
                                                "Log GDP", "Social Support",
                                                "Healthy Life Expectancy", "Freedom To Make Life Choices",
                                                "Generosity", "Perceptions Of Corruption"])


print(HappyDataPd)

HappyDataPd["Score"] = pd.to_numeric(HappyDataPd["Score"], errors="coerce")
HappyDataPd["Log GDP"] = pd.to_numeric(HappyDataPd["Log GDP"], errors="coerce")
least_happy_10 = HappyDataPd.sort_values("Score").head(10)
HappyDataPd["Social Support"] = pd.to_numeric(
    HappyDataPd["Social Support"], errors="coerce")

print(least_happy_10[["Country", "Score"]])

sum_of_happiness = HappyDataPd["Score"].sum()
total_nu_country = len(HappyDataPd)
print(total_nu_country)
avg = sum_of_happiness/total_nu_country
print(f"Average Hapiness {avg}")

# Median
median_score = HappyDataPd["Score"].median()
above_meadian = HappyDataPd[HappyDataPd["Score"] > median_score]

HappyDataPd = HappyDataPd.sort_values("Score", ascending=False)


plt.figure(figsize=(25, 8))
plt.bar(HappyDataPd["Country"], HappyDataPd["Score"], color="skyblue")
plt.xticks(rotation=90)
plt.xlabel("Country")
plt.ylabel("Happiness Score")
plt.title("Happpiness Score Across Whole Country")
plt.tight_layout()
plt.show()


# SCatterPlot

plt.figure(figsize=(25, 8))
plt.scatter(HappyDataPd["Log GDP"], HappyDataPd["Score"])
plt.xlabel("Log Gdp")
plt.ylabel("Score")
plt.title("LOG GDP VS Score ")
plt.show()


# Top 10
top_10 = HappyDataPd.sort_values(by="Score", ascending=False).head(10)
bottom_10 = HappyDataPd.sort_values("Score").head(10)

plt.figure(figsize=(26, 8))
plt.boxplot([top_10["Social Support"], bottom_10["Social Support"]])
plt.xticks([1, 2], ["Top 10 Happiest", "Bottom 10 least Happy"])
plt.ylabel("Social Support")
plt.title("Social Support Comparisoin")
plt.show()

fig = px.choropleth(
    HappyDataPd,
    locations="Country",
    locationmode="country names",
    color="Score",
    title="Happiness Score",
)

fig.show()

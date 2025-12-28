import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

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

df = pd.DataFrame(happy_data, columns=[
    "Overall Rank", "Country", "Score",
    "Log GDP", "Social Support",
    "Healthy Life Expectancy", "Freedom To Make Life Choices",
    "Generosity", "Perceptions Of Corruption"
])

# Print All The Dataset
print(df.head())


df["Score"] = pd.to_numeric(df["Score"], errors="coerce")
# Least Happyy 10 Countries
least_happy_10 = df.sort_values("Score").head(10)
print(least_happy_10[["Country", "Score"]])

# Average Score Of Happiness

sum_of_happiness = df["Score"].sum()
total_number_of_countries = len(df["Country"])
avg = sum_of_happiness/total_number_of_countries
print(f"Average Happpiness {avg}")

# Filter countries above median
median_score = df["Score"].median()
above_median = df[df["Score"] > median_score]
print(above_median[["Country", "Score"]])

# Sort by score for better visualization
df = df.sort_values("Score", ascending=False)


# Plot bar chart
plt.figure(figsize=(25, 8))
plt.bar(df["Country"], df["Score"], color="skyblue")
plt.xticks(rotation=90)  # Rotate country names for readability
plt.xlabel("Country")
plt.ylabel("Happiness Score")
plt.title("Happiness Scores Across Countries (2019)")
plt.tight_layout()
plt.show()


df["Log GDP"] = pd.to_numeric(df["Log GDP"], errors="coerce")
plt.figure(figsize=(8, 5))
plt.scatter(df["Log GDP"], df["Score"])
plt.xlabel("Log GDP")
plt.ylabel("Happiness Score")
plt.title("Correlation: Log GDP vs Happiness Score")
plt.grid(True)
plt.show()

import pandas as pd

data = {
    'country': ['NOR', 'GER', 'CHN'],
    'Gold': [16, 12, 9],
    'Silver': [8, 10, 4],
    'Bronze': [13, 5, 2]
}

df = pd.DataFrame(data)

print(f"Data Frame \n {df}")

print(f"Selecting data elem \n {df.iloc[[0, 2], [0, 2]]}")

print(df[df["country"] == 'CHN'])

country = input("Enter Country")

print(df[df["country"] == f"{country}"])

result = df[df["Gold"] > 10][["country", "Gold"]]
print(f"Countries With More than 10 Gold {result}")

sortBronze = df.sort_values(by='Bronze', ascending=False)
print(f"Sorted Values {sortBronze}")


# print(f"Selecting Second Row \n {df.loc[2]}")

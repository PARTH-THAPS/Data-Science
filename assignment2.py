import pandas as pd


# Excercise 1

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


# Excercise 2

File = pd.read_csv("/Users/user/Downloads/Beijing1.csv", sep=';')

File["Total"] = File["Gold"]+File["Silver"]+File["Bronze"]

print(File)


File.sort_values(by=["Total", "Gold"], ascending=[False, False])


print(f"Sort Medal tally {File}")


total_gold = File["Gold"].sum()
total_silver = File["Silver"].sum()
total_bronze = File["Bronze"].sum()

# 2. Calculate the overall number of medals
total_medals = total_gold + total_silver + total_bronze

print(f"Total Gold medals: {total_gold}")
print(f"Total Silver medals: {total_silver}")
print(f"Total Bronze medals: {total_bronze}")
print(f"Overall total medals: {total_medals}")

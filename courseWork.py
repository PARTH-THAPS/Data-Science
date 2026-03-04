import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("/Users/user/Downloads/spotify.csv")


# Data Will be given by Head
print(data.head())

# Column Info will given
print(data.info())

# mean has been given
print(data.describe())

print("Duplicate ")
print(len(data[data["track_id"].duplicated()]))

data = data.drop_duplicates(subset="track_id").reset_index(drop=True)
print("Duplicate ")
print(data[data["track_id"].duplicated()])


data["track_album_release_date"] = pd.to_datetime(
    data["track_album_release_date"], errors="coerce")
data["release_year"] = data["track_album_release_date"].dt.year

data["track_popularity"] = pd.to_numeric(
    data["track_popularity"], errors="coerce")


plt.figure(figsize=(25, 8))
plt.hist(data["track_popularity"], bins=10)
plt.xlabel("Track Popularity")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


correlation_matrix = data.select_dtypes(include="number")

Corr_matrix = round(correlation_matrix.corr(), 2)


plt.figure(figsize=(10, 8))
sns.heatmap(Corr_matrix, cmap="coolwarm")
plt.show()


data['track_name'] = data["track_name"].astype(str)
print(data.head())

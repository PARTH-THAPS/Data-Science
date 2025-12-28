import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

spotify_file = pd.read_csv("/Users/user/Downloads/spotify.csv")

# No Missing Values Were Found Using The .info() Method
spotify_file.info()

# Need to check the rows in the file before making any changes
print(len(spotify_file))

print(spotify_file.loc[
    spotify_file["track_id"].duplicated(),
    "track_id"
])


spotify_file = (spotify_file.drop_duplicates(
    subset="track_id", keep="first").reset_index(drop=True))


# Need To Check How Many Rows Are Left After Making The Changes
print(len(spotify_file))


# Validated All
print(spotify_file.loc[spotify_file["track_id"].duplicated(), "track_id"])


# Object has been converted into Date Time
spotify_file["track_album_release_date"] = pd.to_datetime(
    spotify_file["track_album_release_date"], errors="coerce")


# To validate Data type of the track_album_release_date
# spotify_file.info()

spotify_file["release_year"] = spotify_file["track_album_release_date"].dt.year

spotify_file["track_popularity"] = pd.to_numeric(
    spotify_file["track_popularity"],
    errors="coerce"
)


top_20 = spotify_file.sort_values(
    by="track_popularity", ascending=False
).head(20)


spotify_release_year = spotify_file.sort_values(
    by="release_year", ascending=True)


year = 2024

all_year_songs = spotify_release_year[spotify_release_year["release_year"] == year]

# 2025 Top 5 Singers
top_5_artists = (
    all_year_songs
    .groupby("track_artist")["track_popularity"]
    .mean()
    .sort_values(ascending=False)
    .head(5)
)


# plt.figure(figsize=(6, 4))
# plt.bar(top_20["track_name"], top_20["track_popularity"])
# plt.xticks(rotation=90)
# plt.xlabel("Track Name")
# plt.ylabel("Track Popularity")
# plt.grid(True)
# plt.show()


# plt.figure(figsize=(6, 4))
# plt.hist(top_5_artists["track_popularity"].dropna(), bins=10)
# plt.xlabel("Track Popularity")
# plt.ylabel("Frequency")
# plt.title("Track Popularity Distribution (Top 5 Artists, 2024)")
# plt.grid(True)
# plt.show()


corelation_matrix = spotify_file.select_dtypes(include="number")

# Correlation Matrix
# Corr_Matrix = round(corelation_matrix.corr(), 2)
# print(Corr_Matrix)


# plt.figure(figsize=(10, 8))
# sns.heatmap(Corr_Matrix, annot=True, cmap="coolwarm",
#             fmt=".2f", linewidths=0.5)
# plt.title("Correlation Heatmap of Spotify Audio Features")
# plt.show()


# Clustering ( K means + PCA )


#  To check if there is null empty cell

features = ['danceability', 'energy', 'valence', 'tempo',
            'acousticness', 'instrumentalness', 'liveness']

feature_required_learning = spotify_file[features]
removed_values = feature_required_learning.dropna(axis=0)

# To validate if data is clean
missing_values = removed_values.isnull().sum()
print(missing_values)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(removed_values)


# Step 3: Run K-Means (k=4)
k = 4
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

# Add cluster labels to the DataFrame
removed_values['cluster'] = clusters

# PCA for 2D visualization
pca = PCA(n_components=2, random_state=42)
pca_result = pca.fit_transform(scaled_features)

pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])
pca_df['cluster'] = clusters

plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='PC1', y='PC2',
    hue='cluster',
    palette='Set2',
    data=pca_df,
    s=60,
    alpha=0.8
)
plt.title("Spotify Songs Clusters (K-Means + PCA)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title='Cluster')
plt.grid(True)
plt.show()


removed_values.info()

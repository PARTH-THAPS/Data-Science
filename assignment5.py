import pandas as pd
import matplotlib.pyplot as plt

economic_freedom_file = pd.read_csv(
    "/Users/user/Downloads/economic_freedom.csv")
world_happiness_file = pd.read_csv(
    "/Users/user/Downloads/world_happiness.csv")


print(world_happiness_file)

# Show real column names to debug
print("Column names:")
print(world_happiness_file.columns.tolist())

# Automatically detect ranking-type columns
rank_cols = [
    col for col in world_happiness_file.columns if "rank" in col.lower()]
print("Detected ranking columns:", rank_cols)

# Delete ranking column(s)
print(world_happiness_file.drop(columns=rank_cols).describe())


# ============
# FIX MISSING VALUES
# ============

print("\n=== Missing Values (Economic Freedom) ===")
print(economic_freedom_file.isnull().sum())

print("\n=== Missing Values (World Happiness) ===")
print(world_happiness_file.isnull().sum())


# 1) DROP COLUMNS with >40% missing
economic_freedom_file = economic_freedom_file.dropna(
    axis=1, thresh=len(economic_freedom_file) * 0.6
)
world_happiness_file = world_happiness_file.dropna(
    axis=1, thresh=len(world_happiness_file) * 0.6
)


# 2) DROP ROWS with >50% missing
economic_freedom_file = economic_freedom_file.dropna(
    thresh=economic_freedom_file.shape[1] * 0.5
)
world_happiness_file = world_happiness_file.dropna(
    thresh=world_happiness_file.shape[1] * 0.5
)


# 3) IMPUTE remaining missing values
# Numeric → mean
economic_freedom_file = economic_freedom_file.fillna(
    economic_freedom_file.mean(numeric_only=True)
)
world_happiness_file = world_happiness_file.fillna(
    world_happiness_file.mean(numeric_only=True)
)

# Categorical → mode (most frequent)
economic_freedom_file = economic_freedom_file.fillna(
    economic_freedom_file.mode()
)
world_happiness_file = world_happiness_file.fillna(
    world_happiness_file.mode()
)


print("\n=== Missing Values AFTER Fixing (Economic Freedom) ===")
print(economic_freedom_file.isnull().sum())

print("\n=== Missing Values AFTER Fixing (World Happiness) ===")
print(world_happiness_file.isnull().sum())


# ============
# DTYPE SPLITTING
# ============

economic_freedom_numeric = economic_freedom_file.select_dtypes(include=[
                                                               "number"])
economic_freedom_file_categorical = economic_freedom_file.select_dtypes(exclude=[
                                                                        "number"])

world_numeric = world_happiness_file.select_dtypes(include=["number"])
world_categorical = world_happiness_file.select_dtypes(exclude=["number"])

print("\n--- World Happiness Numeric Columns ---")
print(world_numeric.columns.tolist())

print("\n--- World Happiness Categorical Columns ---")
print(world_categorical.columns.tolist())

print("\n--- Economic Freedom Numeric Columns ---")
print(economic_freedom_numeric.columns.tolist())

print("\n--- Economic Freedom Categorical Columns ---")
print(economic_freedom_file_categorical.columns.tolist())

numeric_cols = world_numeric.columns.tolist()

for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    plt.boxplot(world_happiness_file[col], vert=False)
    plt.title(f'Boxplot of {col}')
    plt.xlabel(col)
    plt.show()

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

# To upload files in Google Colab
uploaded = files.upload()
filename = list(uploaded.keys())[0]

# Read data from CSV file
df = pd.read_csv(filename)

# Display first 10 rows
print(df.head(10))

# Check for any null values in each column
print(df.isnull().any())

# Visualize missing values using a heatmap
subset = df.iloc[:5200, :]  # Taking the first 5200 rows
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values in Student Dataset")
plt.show()

# Display first 10 rows
print(df.head(10))

# Drop rows where all values are NaN
df_no_empty = df.dropna(how="all")
print(df_no_empty)

# Fill missing values using backward fill method
df_filled = df_no_empty.bfill()
print(df_filled)

# Interpolate missing values
df_interpolated = df_filled.interpolate()
print(df_interpolated)

# Drop all rows with any NaN values
df_dropped = df_interpolated.dropna()
print(df_dropped)

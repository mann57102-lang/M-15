# Load Basic Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from google.colab import files

warnings.filterwarnings('ignore')

# Upload File
uploaded = files.upload()

# Reading the CSV file
filename = list(uploaded.keys())[0]
df = pd.read_csv(filename)

# Display first few rows
print(df.head())

# Display dataset shape
print(df.shape)

# Display column names
print(df.columns)

# Display descriptive statistics
print(df.describe())

# Check for null values
print(df.isnull().sum())

# Display dataset information
print(df.info())

# Create histograms
df.hist(figsize=(12, 12), layout=(5, 3))
plt.tight_layout()
plt.show()

# Create box and whiskers plots
df.select_dtypes(include=np.number).plot(
    kind='box',
    subplots=True,
    layout=(5, 3),
    figsize=(12, 12)
)
plt.tight_layout()
plt.show()

# Create bar plot
sns.barplot(data=df, x='gender', y='math score', hue='test preparation course', palette='spring')
plt.title('Average Maths Score by Gender and Test Preparation')
plt.show()

# Display value counts for gender column
print(df['gender'].value_counts())

# Display value counts for test preparation course
print(df['test preparation course'].value_counts())

# Display value counts for lunch
print(df['lunch'].value_counts())

# Create correlation heatmap for numerical columns
plt.figure(figsize=(12, 8))
sns.heatmap(
    df.select_dtypes(include=np.number).corr(),
    annot=True,
    cmap='terrain'
)
plt.title('Student Performance Correlation Heatmap')
plt.show()

# Create countplot for gender vs test preparation
sns.countplot(
    x='gender',
    data=df,
    palette='husl',
    hue='test preparation course'
)
plt.title('Gender vs Test Preparation')
plt.show()

# Create countplot for parental level of education
sns.countplot(x='parental level of education', data=df, palette='BuGn')
plt.xticks(rotation=45)
plt.title('Students by Parental Education')
plt.show()

# Create countplot for lunch type vs gender
sns.countplot(x='lunch', hue='gender', data=df)
plt.title('Lunch Type by Gender')
plt.show()

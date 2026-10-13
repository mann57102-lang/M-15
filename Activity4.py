import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

# Upload File
uploaded = files.upload()
filename = list(uploaded.keys())[0]

# Read the uploaded file
countries_df = pd.read_csv(filename)

countries = countries_df

print(countries.head(3))

# Extract rows where the year is 1952
c_52 = countries.loc[countries['year'] == 1952]
print(c_52.head())

# Extract rows where the year is 2007
c_07 = countries.loc[countries['year'] == 2007]
print(c_07.head())

# Merge the 1952 and 2007 dataframes together
c_merge = c_52.merge(
    c_07,
    on='country',
    suffixes=('_1952', '_2007')
)

print(c_merge.head())

# Calculate GDP per capita growth
c_merge['gdp_growth'] = (
    c_merge['gdpPercap_2007'] - c_merge['gdpPercap_1952']
)

print(c_merge.head())

# Sort values and get the 10 countries with the biggest GDP growth
c_merge = c_merge.sort_values(
    'gdp_growth',
    ascending=False
).head(10)

print(c_merge[['country', 'gdp_growth']])

# Reset the index
c_merge = c_merge.reset_index(drop=True)

# Top 10 countries with the highest GDP per capita growth
print(c_merge[['country', 'gdp_growth']])

# Plot the data
names = c_merge['country']
gdp_grow = c_merge['gdp_growth']

plt.figure(figsize=(15, 9))

plt.bar(names, gdp_grow, width=0.6, color='orange')

plt.xlabel('Country')
plt.ylabel('GDP per Capita Growth ($)')
plt.title(
    'Top 10 Countries with the Biggest GDP per Capita Growth (1952–2007)'
)

plt.xticks(rotation=45)

# Add values above each bar
for x, y in zip(names, gdp_grow):
    label = "{:.2f}".format(y)

    plt.annotate(
        label,
        (x, y),
        textcoords="offset points",
        xytext=(0, 10),
        ha='center'
    )

plt.tight_layout()
plt.show()

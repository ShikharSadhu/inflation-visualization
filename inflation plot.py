import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

# Load the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\Shikhar Sadhu\Documents\Shikhar\inflation project\inflation.csv", skiprows=4, header=0)

# Select specific countries
countries = ['Japan', 'United States', 'Canada', 'India', 'Germany', 'Italy']

# Filter the DataFrame for the selected countries
df_filtered = df[df['Country Name'].isin(countries)]

# Drop unnecessary columns
df_filtered = df_filtered.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])

# Drop rows and columns with all NaN values
df_filtered = df_filtered.dropna()

# Reset the index of the DataFrame
df_filtered = df_filtered.reset_index(drop=True)

print(df_filtered.head())

# Melt the DataFrame to long format
df_melted = df_filtered.melt(
    id_vars=['Country Name'],
    var_name='Year',
    value_name='Inflation Rate'
    )

# Convert 'Year' to int type
df_melted['Year'] = df_melted['Year'].astype(int)


# Create the bar plot
plt.figure(figsize=(25, 8))
bar_df = df_melted[df_melted['Year'] >= 1980]  # Filter for years >= 1980
sns.barplot(data=bar_df, x='Year', y='Inflation Rate', hue='Country Name', width=0.8)

# Set the title and labels
plt.title('Inflation Over Time')
plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')

# Rotate x-ticks for better readability
plt.xticks(rotation=45)
plt.tight_layout()

# Show the legend
plt.legend(title='Country', loc='best')

# Set the grid for better readability
plt.grid(True)

# Save the bar plot as an image
plt.savefig("inflation_chart.png")

# Show the plot
plt.show()


# Line plot for inflation rates
plt.figure(figsize=(14, 8))

# Create the line plot
sns.lineplot(data=df_melted, x='Year', y='Inflation Rate', hue='Country Name', marker='o')

# Set the title and labels for the line plot
plt.title('Inflation Trends Over Time')
plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')

# Rotate x-ticks for better readability
plt.xticks(rotation=45)
plt.tight_layout()

# Show the legend
plt.legend(title='Country', loc='best')

# Set the grid for better readability
plt.grid(True)

# Save the line plot as an image
plt.savefig("inflation_trends.png")

# Show the line plot
plt.show()


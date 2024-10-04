import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the CSV file
file_path = r'C:\Users\HP\Desktop\Ghuhan\global_income_inequality.csv'
data = pd.read_csv(file_path)

# Show the first few rows and the columns of the dataset to understand its structure
data.head(), data.columns

# 9. Country Ranking based on Gini Index (latest year available for each country)
latest_year_data = data.loc[data.groupby('Country')['Year'].idxmax()]
gini_ranking = latest_year_data[['Country', 'Year', 'Gini Index']].sort_values(by='Gini Index', ascending=False)

# 5. Country-wise Comparison (Average Income, Gini Index, and Population)
country_comparison = latest_year_data[['Country', 'Average Income (USD)', 'Gini Index', 'Population']].sort_values(by='Gini Index')

# 8. Time-Series Analysis for inequality (Gini Index) and average income
# Let's select a sample of countries for visualization
sample_countries = ['United States', 'India', 'Brazil', 'Germany', 'China']
time_series_data = data[data['Country'].isin(sample_countries)]

# Plotting code for visualizations

def plot_country_ranking(gini_ranking):
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Gini Index', y='Country', hue='Country', data=gini_ranking, palette='viridis', dodge=False, legend=False)
    plt.title('Country Ranking by Gini Index (Latest Year Available)')
    plt.xlabel('Gini Index')
    plt.ylabel('Country')
    plt.show()

def plot_country_comparison(country_comparison):
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='Average Income (USD)', y='Gini Index', size='Population', hue='Country', data=country_comparison, palette='viridis', sizes=(40, 200))
    plt.title('Country-wise Comparison of Gini Index vs Average Income (Latest Year Available)')
    plt.xlabel('Average Income (USD)')
    plt.ylabel('Gini Index')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

def plot_time_series_analysis(time_series_data):
    plt.figure(figsize=(12, 8))
    
    # Plot Gini Index over time for the selected countries
    plt.subplot(2, 1, 1)
    sns.lineplot(x='Year', y='Gini Index', hue='Country', data=time_series_data, marker='o')
    plt.title('Gini Index over Time for Selected Countries')
    plt.ylabel('Gini Index')
    plt.xlabel('Year')

    # Plot Average Income over time for the selected countries
    plt.subplot(2, 1, 2)
    sns.lineplot(x='Year', y='Average Income (USD)', hue='Country', data=time_series_data, marker='o')
    plt.title('Average Income over Time for Selected Countries')
    plt.ylabel('Average Income (USD)')
    plt.xlabel('Year')

    plt.tight_layout()
    plt.show()

# Generate visualizations
plot_country_ranking(gini_ranking)
plot_country_comparison(country_comparison)
plot_time_series_analysis(time_series_data)

# Return the data results for operations 9, 5, and 8
gini_ranking.head(), country_comparison.head(), time_series_data.head()

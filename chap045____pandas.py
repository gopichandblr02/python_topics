"""
Python Pandas with Examples
Pandas is a powerful library in Python used for data manipulation and analysis. It provides data structures like DataFrame
and Series that make it easy to handle structured data (e.g., CSV files, Excel files, SQL databases, etc.).

1. Installing Pandas
If you don't have Pandas installed, you can install it using pip:
"""
### pip install pandas

# 2. Importing Pandas
import pandas as pd
# 3. Creating a DataFrame
"""
A DataFrame is a 2D table (like a spreadsheet) with rows and columns.
Example: Creating DataFrame from a Dictionary
"""
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)
# Output:
#       Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
#
# Example: Creating DataFrame from a List of Lists

import pandas as pd
data = [['Alice', 25, 'New York'], ['Bob', 30, 'Los Angeles'], ['Charlie', 35, 'Chicago']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)
"""
Output:
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
4. Reading Data from Files
Pandas makes it easy to read data from various file formats such as CSV, Excel, and JSON.
Example: Reading a CSV File
"""
import pandas as pd
# Assuming you have a file 'data.csv'
df = pd.read_csv('data.csv')
print(df)

# Example: Reading an Excel File
import pandas as pd
df = pd.read_excel('data.xlsx')
print(df)

#Example: Reading a JSON File
import pandas as pd
df = pd.read_json('data.json')
print(df)
"""
5. Basic DataFrame Operations
View first/last few rows
"""
# View first 5 rows
print(df.head())

# View last 5 rows
print(df.tail())
# Select a Single Column

print(df['Name'])  # Select column 'Name'
# Select Multiple Columns

print(df[['Name', 'City']])  # Select columns 'Name' and 'City'
# Filtering Data
# Filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)
# Set Index
# Set the 'Name' column as the index
df.set_index('Name', inplace=True)
print(df)
"""
6. DataFrame Manipulation
Adding a New Column
"""
df['Salary'] = [70000, 80000, 90000]
print(df)

#Modifying Existing Column
df['Age'] = df['Age'] + 1  # Increment age by 1
print(df)

#Dropping a Column
df.drop(columns=['Salary'], inplace=True)  # Drop the 'Salary' column
print(df)
"""
7. Descriptive Statistics
Pandas provides various methods to perform basic statistical analysis on your data.
Example: Basic Statistics
"""
# Get descriptive statistics for numerical columns
print(df.describe())
# Example: Mean, Median, and Mode
print(df['Age'].mean())    # Mean of Age
print(df['Age'].median())  # Median of Age
print(df['Age'].mode())    # Mode of Age
"""
8. Handling Missing Data
Detecting Missing Data
"""
# Check for missing values in each column
print(df.isnull())
# Count the number of missing values
print(df.isnull().sum())
# Filling Missing Data
# Fill missing values with a specific value
df.fillna('Unknown', inplace=True)
# Dropping Missing Data
# Drop rows with any missing value
df.dropna(inplace=True)
"""
9. Grouping Data
Example: Grouping by a Column
"""
# Group by 'City' and calculate the mean Age for each group
grouped = df.groupby('City')['Age'].mean()
print(grouped)
# Example: Aggregating Data

# Group by 'City' and calculate multiple aggregations
aggregated = df.groupby('City').agg({'Age': ['min', 'max', 'mean']})
print(aggregated)
"""
10. Merging DataFrames
You can merge DataFrames using common columns or indices.
Example: Merging DataFrames
"""
# DataFrames with a common column 'ID'
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Age': [25, 30, 35]})
merged_df = pd.merge(df1, df2, on='ID', how='inner')  # Merging on 'ID'
print(merged_df)
#
# Output:
#    ID     Name  Age
# 0   1    Alice   25
# 1   2      Bob   30
"""
11. Pivot Tables
Pivot tables allow you to summarize and aggregate data.
Example: Creating a Pivot Table
"""
df = pd.DataFrame({
    'City': ['New York', 'New York', 'Chicago', 'Chicago'],
    'Year': [2020, 2021, 2020, 2021],
    'Sales': [250, 300, 150, 200]
})

pivot = pd.pivot_table(df, values='Sales', index='City', columns='Year', aggfunc='sum')
print(pivot)
# Output:
#
# Year        2020  2021
# City
# Chicago      150   200
# New York     250   300
"""
12. Writing Data to Files
Example: Writing to CSV
"""
df.to_csv('output.csv', index=False)
# Example: Writing to Excel

df.to_excel('output.xlsx', index=False)
# Example: Writing to JSON

df.to_json('output.json', orient='records')
"""
13. Sorting Data
Example: Sorting by Column
"""
# Sort by 'Age' in ascending order
sorted_df = df.sort_values(by='Age')
print(sorted_df)
"""
14. Plotting Data
Pandas integrates well with Matplotlib for data visualization.
"""
# Example: Plotting Data
import matplotlib.pyplot as plt

# Plot a bar chart of Age
df['Age'].plot(kind='bar')
plt.show()

"""
When to Use Pandas?
Data Cleaning: Handling missing or duplicate data.
Data Analysis: Aggregating, grouping, and summarizing data.
Data Transformation: Merging, reshaping, and pivoting data.
Data Export: Reading from and writing to various file formats (CSV, Excel, JSON).
Pandas is an essential tool for data manipulation and analysis in Python!
"""
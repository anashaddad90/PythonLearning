import pandas as pd

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Salary': [70000, 80000, 120000, 100000]
}

df = pd.DataFrame(data)
print(df)

#Filtering Data
filtered = df[(df['Salary'] > 80000) & (df['Age'] > 30)]
print(filtered)

#Add Column
df['Bonus'] = df['Salary']* 0.1
print(df)

#Modify Column
df['Salary'] = df['Salary'] * 1.05
print(df)

#GroupBy
grouped = df.groupby('City')['Salary'].mean()
print(grouped)

#Aggregation
city_count = df.groupby('City').size()
print(city_count)

#Sorting
sorted_df = df.sort_values('Salary', ascending=False)
print(sorted_df)

#Merging
new_data = {
    'Name': ['Alice', 'Charlie'],
    'Department': ['HR', 'Engineering']
}
df2 = pd.DataFrame(new_data)
merged = pd.merge(df, df2, on='Name', how='left')
print(merged)

#Handling Missing Data
df_with_missing = merged.copy()
df_with_missing['Department'] = df_with_missing['Department'].fillna('Unknown')
print(df_with_missing)

#Reshaping Data (Pivot Table)
pivot = df.pivot_table(values='Salary', index='Age', columns='City', aggfunc='mean')
print(pivot)

# Working with Dates
df['Date'] = pd.date_range(start='2024-01-01', periods=len(df))
print(df)

# Filter by a specific date range
filtered_by_date = df[df['Date'] >= '2024-01-02']
print(filtered_by_date)
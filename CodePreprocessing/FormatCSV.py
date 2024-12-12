import pandas as pd

# Read the original CSV file with ";" as the delimiter
data = pd.read_csv('Datasets/bank-full.csv', sep=';', engine='python')

# Overwrite the original CSV file with properly separated columns
data.to_csv('Datasets/bank-full.csv', index=False)

# Display the first few rows to confirm the changes
print(data.head())
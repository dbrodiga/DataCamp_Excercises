import pandas as pd
column_names = ['Name', 'Sector', 'Price', 'EPS']
df = pd.read_csv(r'H:\UCD Professional Academy\DataCamp Excercise data\Introduction to Python for Finance\S&P100.csv', names=column_names)
sectors = df['Sector']
names = df['Name']
prices = df['Price']

print(prices)
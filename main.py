# Import the data
import pandas as pd
column_names = ['Name', 'Sector', 'Price', 'EPS']
df = pd.read_csv('S&P100.csv', names=column_names)
# Import the data
import pandas as pd
# Peak at top five rows
alphabet = pd.read_csv('HistoricalQuotes.csv', index_col=0)
print(alphabet.head())
print(alphabet.info())
print(alphabet.describe())

print(alphabet.columns)
print(alphabet.index)
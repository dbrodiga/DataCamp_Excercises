# Import the data
import pandas as pd
import matplotlib.pyplot as plt
# Peak at top five rows
avocados = pd.read_pickle('avoplotto.pkl')

# Check individual values for missing values
print(avocados.isna())

# Check each column for missing values
print(avocados.isna().any())

# Bar plot of missing values by variable
avocados.isna().sum().plot(kind="bar")

# Show plot
plt.show()
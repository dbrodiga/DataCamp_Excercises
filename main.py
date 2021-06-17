# Import the data
import pandas as pd
import matplotlib.pyplot as plt
# Peak at top five rows
avocados = pd.read_pickle('avoplotto.pkl')
avocados[['date']] = avocados[['date']].astype('datetime64')
avocados['year'] = avocados['date'].dt.year
print(avocados.info())
avocados_2016 = avocados[avocados['date'].dt.year == '2016']
print(avocados_2016.info())




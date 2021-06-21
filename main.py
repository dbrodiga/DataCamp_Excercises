# Import the data
import pandas as pd
import matplotlib.pyplot as plt

taglines = pd.read_pickle('DataCamp M4/taglines.p')
movies = pd.read_pickle('DataCamp M4/movies.p')

movies_taglines = movies.merge(taglines, on='id', how='left')
print(movies_taglines.head())

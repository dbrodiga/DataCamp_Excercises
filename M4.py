import pandas as pd
import matplotlib.pyplot as plt

wards = pd.read_pickle('DataCamp M4/ward.p')
census = pd.read_pickle('DataCamp M4/census.p')
licenses = pd.read_pickle('DataCamp M4/licenses.p')
biz_owners = pd.read_pickle('DataCamp M4/business_owners.p')
taxi_owners = pd.read_pickle('DataCamp M4/taxi_owners.p')
taxi_veh = pd.read_pickle('DataCamp M4/taxi_vehicles.p')

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own', '_veh'))

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

wards_census = wards.merge(census, on='ward')
print(wards_census.info())
# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)

ward_licenses = wards.merge(licenses, on='ward', suffixes=('_ward', '_lic'))
print(ward_licenses.head())

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values('account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

cal = pd.read_pickle('DataCamp M4/cta_calendar.p')
ridership = pd.read_pickle('DataCamp M4/cta_ridership.p')
stations = pd.read_pickle('DataCamp M4/stations.p')

ridership_cal_stations = ridership.merge(cal, on=(['year', 'month', 'day'])) \
    .merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7)
                   & (ridership_cal_stations['day_type'] == 'Weekday')
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

zip_demo = pd.read_pickle('DataCamp M4/zip_demo.p')
# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
            			.merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))

land_use = pd.read_pickle('DataCamp M4/land_use.p')

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                        .merge(licenses, on='ward', suffixes=('_cen', '_lic'))

#Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward', 'pop_2010', 'vacant'],
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant','account','pop_2010'],
                                             ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())

taglines = pd.read_pickle('DataCamp M4/taglines.p')
movies = pd.read_pickle('DataCamp M4/movies.p')
financials = pd.read_pickle('DataCamp M4/financials.p')
movie_to_genres = pd.read_pickle('DataCamp M4/movie_to_genres.p')

movies_taglines = movies.merge(taglines, on='id', how='left')
print(movies_taglines.head())

# Merge movies and financials with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(movies, how='right',
                                      left_on='movie_id',
                                      right_on='id')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()

crews = pd.read_pickle('DataCamp M4/crews.p')

# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') &
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())

sequels = pd.read_pickle('DataCamp M4/sequels.p')

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', right_on='id', suffixes=('_org', '_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff', ascending=False).head())
# Example 1, do not modify!
import numpy as numpy

print(8 / 2)

# Example 2, do not modify!
print(2 ** 2)

# Addition, no print output
print(10 + 2)

# Multiplication, with print output
james = 10 * 2
print(james)
print(10 * 2)

# Create the variable total and print the total revenue
# Define the 3 variables
revenue_1 = 229.23
revenue_2 = 177.86
revenue_3 = 89.95
total = (revenue_1 + revenue_2 + revenue_3)
print(total)

# Print the average revenue
average = total / 3
print(average)

# Create company_1
company_1 = 'Apple'
print(company_1)

# Create year_1
year_1 = 2017
print(year_1)

# Create revenue_1
revenue_1 = 229.23
print(revenue_1)

# Type of company_1
print(type(company_1))

# Type of year_1
print(type(year_1))

# Type of revenue_1
print(type(revenue_1))

# Test equality
test_company = 'apple'
print(company_1)
print(test_company == company_1)

# Compare revenue_1 and revenue_2
print(revenue_1 > revenue_2)

# Update data types
year_1_str = str(year_1)
revenue_1_str = str(revenue_1)

# Create a complete sentence combining only the string data types
sentence = 'The revenue of ' + company_1 + ' in ' + year_1_str + ' was $' + revenue_1_str + ' billion.'

# Print sentence
print(sentence)

# Module 1 Chapter 2
# Create and print list names
names = ['Apple Inc', 'Coca-Cola', 'Walmart']
print(names)

# Create and print list prices
prices = [159.54, 37.13, 71.17]
print(prices)

# Print the first item in names
print(names[0])

# Print the second item in names
print(names[1])

# Print the last element in prices
print(prices[-1])

# names
names = ['Apple Inc', 'Coca-Cola', 'Walmart']

# Use slicing on list names
names_subset = names[1:]
print(names_subset)

# prices
prices = [159.54, 37.13, 71.17]

# Use extended slicing on the list prices
prices_subset = prices[0:2]
print(prices_subset)

# Create and print the nested list stocks
stocks = [names, prices]
print(stocks)

# Use list indexing to obtain the list of prices
print(stocks[1])

# Use indexing to obtain company name Coca-Cola
print(stocks[0][1])

# Use indexing to obtain 71.17
print(stocks[1][2])

# Print the sorted list prices
prices = [159.54, 37.13, 71.17]
prices.sort()
print(prices)

# Find the maximum price in the list price
prices = [159.54, 37.13, 71.17]
price_max = max(prices)
print(price_max)

# Append a name to the list names
names.append('Amazon.com')
print(names)

# Extend list names
more_elements = ['DowDuPont', 'Alphabet Inc']
names.extend(more_elements)
print(names)

# Do not modify this
max_price = max(prices)

# Identify index of max price
max_index = prices.index(max_price)

# Identify the name of the company with max price
max_stock_name = names[max_index]

# Fill in the blanks
print('The largest stock price is associated with ' + max_stock_name + ' and is $' + str(max_price) + '.')

# Import numpy as np
import numpy as np

# Lists
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]

# NumPy arrays
prices_array = np.array(prices)
earnings_array = np.array(earnings)

# Print the arrays
print(prices_array)
print(earnings_array)

# Import numpy as np
import numpy as np

# Create PE ratio array
pe_array = prices_array / earnings_array

# Print pe_array
print(pe_array)

# Subset the first three elements
prices_subset_1 = prices_array[0:3]
print(prices_subset_1)

# Subset last three elements
prices_subset_2 = prices_array[-3:]
print(prices_subset_2)

# Subset every third element
prices_subset_3 = prices_array[0:7:3]
print(prices_subset_3)

# Create a 2D array of prices and earnings
stock_array = np.array([prices, earnings])
print(stock_array)

# Print the shape of stock_array
print(stock_array.shape)

# Print the size of stock_array
print(stock_array.size)

# Transpose stock_array
stock_array_transposed = np.transpose(stock_array)
print(stock_array_transposed)

# Print the shape of stock_array
print(stock_array_transposed.shape)

# Print the size of stock_array
print(stock_array_transposed.size)

# Subset prices from stock_array_transposed
prices = stock_array_transposed[:, 0]
print(prices)

# Subset earnings from stock_array_transposed
earnings = stock_array_transposed[:, 1]
print(earnings)

# Subset the price and earning for first company
company_1 = stock_array_transposed[0, :]
print(company_1)

# Calculate the mean
prices_mean = np.mean(prices)
print(prices_mean)

# Calculate the standard deviation
prices_std = np.std(prices)
print(prices_std)

# Create and print company IDs
company_ids = np.arange(1, 8, 1)
print(company_ids)

# Use array slicing to select specific company IDs
company_ids_odd = np.arange(1, 8, 2)
print(company_ids_odd)

# Find the mean
price_mean = np.mean(prices)

# Create boolean array
boolean_array = (prices > price_mean)
print(boolean_array)

# Select prices that are greater than average
above_avg = prices[boolean_array]
print(above_avg)

# Import the data
import pandas as pd
column_names = ['Name', 'Sector', 'Price', 'EPS']
df = pd.read_csv(r'H:\UCD Professional Academy\DataCamp Excercise data\Introduction to Python for Finance\S&P100.csv', names=column_names)
sectors = df['Sector']
names = df['Name']
prices = df['Price']
earnings = df['EPS']

# Create boolean array
boolean_array = (sectors == 'Health Care')
print(boolean_array)

# Print only health care companies
health_care = names[boolean_array]
print(health_care)

# Import matplotlib.pyplot with the alias plt
import matplotlib.pyplot as plt
column_names2 = ['Day', 'Price']
df2 = pd.read_csv(r'H:\UCD Professional Academy\DataCamp Excercise data\Introduction to Python for Finance\Stocks1.csv', names=column_names2)
days = df2['Day']
prices_stock = df2['Price']
column_names3 = ['day', 'company1', 'company2']
df3 = pd.read_csv(r'H:\UCD Professional Academy\DataCamp Excercise data\Introduction to Python for Finance\Stocks2.csv', names=column_names3)
days3 = df3['day']
prices1 = df3['company1']
prices2 = df3['company2']

# Plot the price of stock over time
plt.plot(days, prices_stock, color="red", linestyle="--")

# Add x and y labels
plt.xlabel('Days')
plt.ylabel('Prices, $')

# Add plot title
plt.title('Company Stock Prices Over Time')

# Show plot
#plt.show()
plt.close()

# Plot two lines of varying colors
plt.plot(days3, prices1, color='red')
plt.plot(days3, prices2, color='green')

# Add labels
plt.xlabel('Days')
plt.ylabel('Prices, $')
plt.title('Stock Prices Over Time')
#plt.show()
plt.close()

# Plot price as a function of time
plt.scatter(days, prices_stock, color='green', s=0.1)

# Show plot
#plt.show()
plt.close()

# Plot histogram
plt.hist(prices_stock, bins=100)

# Display plot
#plt.show()
plt.close()

# Plot histogram of stocks_A
plt.hist(prices1, bins=100, alpha=0.4)

# Plot histogram of stocks_B
plt.hist(prices2, bins=100, alpha=0.4)

# Display plot
#plt.show()
plt.close()

# Plot stock_A and stock_B histograms
plt.hist(prices1, bins=100, alpha=0.4, label='Stock A')
plt.hist(prices2, bins=100, alpha=0.4, label='Stock B')

# Add the legend
plt.legend()

# Display the plot
#plt.show()
plt.close()

# First four items of names
print(names[0:4])
#print(names)
type(names)

# Print information on last company
print(names[-1:])
print(prices[-1:])
print(earnings[-1:])
print(sectors[-1:])

# Convert lists to arrays
str_prices_array = np.array(prices[1:])
str_earnings_array = np.array(earnings[1:])
str_names_array = np.array(names[1:])

prices_array = str_prices_array.astype(float)
earnings_array = str_earnings_array.astype(float)

print(prices_array)
print(type(prices_array))

print(earnings_array)
print(type(earnings_array))

# Calculate P/E ratio
pe = prices_array / earnings_array
print(pe)

# Create boolean array
boolean_array = (sectors == 'Information Technology')
boolean_array2 = boolean_array[1:]

# Subset sector-specific data
it_names = str_names_array[boolean_array2]
it_pe = pe[boolean_array2]

# Display sector names
print(it_names)
print(it_pe)

# Create boolean array
boolean_array = (sectors == 'Consumer Staples')
boolean_array2 = boolean_array[1:]

# Subset sector-specific data
cs_names = names[boolean_array]
cs_pe = pe[boolean_array2]

# Display sector names
print(cs_names)
print(cs_pe)

it_pe_mean = np.mean(it_pe)
it_pe_std = np.std(it_pe)

print(it_pe_mean)
print(it_pe_std)

cs_pe_mean = np.mean(cs_pe)
cs_pe_std = np.std(cs_pe)

print(cs_pe_mean)
print(cs_pe_std)

# Make a scatterplot
plt.close()
it_id = range(0, 15)
cs_id = range(0, 12)
plt.scatter(it_id, it_pe, color = 'red', label = 'IT')
plt.scatter(cs_id, cs_pe, color = 'green', label = 'CS')

# Add legend
plt.legend()

# Add labels
plt.xlabel('Company ID')
plt.ylabel('P/E Ratio')
#plt.show()
plt.close()

# Plot histogram
plt.hist(x = it_pe, bins = 8)

# Add x-label
plt.xlabel('P/E ratio')

# Add y-label
plt.ylabel('Frequency')

# Show plot
#plt.show()
plt.close()

# Identify P/E ratio within it_pe that is > 50
outlier_price = it_pe[it_pe > 50]

# Identify the company with PE ratio > 50
outlier_name = it_names[it_pe > 50]

print(outlier_name)
print(outlier_price)

outlier_name2 = outlier_name

print(outlier_name2)

print(type(outlier_name2))
print(type(outlier_price))

# Display results
print("In 2017, " + str(outlier_name2) + " had an abnormally high P/E ratio of " + str(round(outlier_price[0], 2)) + ".")


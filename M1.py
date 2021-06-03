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
#import pandas as pd
#df = pd.read_csv(r'H:\UCD Professional Academy\DataCamp Excercise data\Introduction to Python for Finance\S&P100.csv')
#sectors = df.loc[:,1]
#print(sectors)

# Create boolean array
#boolean_array = (sectors == 'Health Care')
#print(boolean_array)

# Print only health care companies
#health_care = names[boolean_array]
#print(health_care)

# Import matplotlib.pyplot with the alias plt
#import matplotlib.pyplot as plt

# Plot the price of stock over time
#plt.plot(days, prices, color="red", linestyle="--")

# Display the plot
#plt.show()

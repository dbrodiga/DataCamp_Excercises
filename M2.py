import datetime

# Date and time now
now = datetime.datetime.now()
print(now)

# Flash crash May 28, 1962
flash_crash = datetime.datetime(1962, 5, 28)
print(flash_crash)

# Black Monday Oct 19, 1987
black_monday = datetime.datetime(1987, 10, 19)
print(black_monday)

crash_text = "Friday the 13th, Oct, 1989"

# Create a format string mapping the text
crash_format_str = "%A the %dth, %b, %Y"
min_crash = datetime.datetime.strptime(crash_text, crash_format_str)
print(min_crash)

recession_text = "07/03/90"

# Create format string
recession_format_str = "%m/%d/%y"

# Create datetime from text using format string
nineties_rec = datetime.datetime.strptime(recession_text, recession_format_str)
print(nineties_rec)

org_text = "Sep 16 1992"

# Format string for original text
org_format = "%b %d %Y"

# Create datetime for Black Wednesday
black_wednesday = datetime.datetime.strptime(org_text, org_format)
print(black_wednesday)

# New format: 'Wednesday, September 16, 1992'
new_format = "%A, %B %d, %Y"

# String in new format
new_text = black_wednesday.strftime(new_format)
print(new_text)

# March 10, 2000 Tech Bubble Crash
tech_bubble = datetime.datetime(2000, 3, 10)

# Access the year
yr  = tech_bubble.year

# Access the month
mth = tech_bubble.month

# Access the day
day = tech_bubble.day

print(f"Year: {yr}, Month: {mth}, Day: {day}")

# Lehman Brothers before Morgan Stanley?
lehman = datetime.datetime(2008, 9, 15)
morgan_stanley = datetime.datetime(2008, 9, 22)
tarp = datetime.datetime(2008, 10, 3)
goldman_sachs = datetime.datetime(2008, 9, 22)
lehman_first = lehman < morgan_stanley

print(f"It is {lehman_first} that Lehman Brothers declared bankruptcy first.")

tarp_first = goldman_sachs > tarp

print(f"It is {tarp_first} that TARP was approved first.")

same_time = goldman_sachs == morgan_stanley

print(f"It is {same_time} that Morgan Stanley and Goldman Sachs acted simultaneously")

from datetime import datetime, timedelta

# Seven days before TARP
week_before = tarp - timedelta(days = 7)

# Print week_before
print(week_before)

# One week after TARP
week_after = tarp + timedelta(weeks = 1)

# Print week_after
print(week_after)

# One year after TARP
year_after = tarp + timedelta(weeks = 52)

# Print year_after
print(year_after)

cusip_lookup = {}

# Alphabet
cusip_lookup['38259P706'] = 'GOOG'

print(cusip_lookup)

# Apple
cusip_lookup['037833100'] = 'AAPL'

print(cusip_lookup)

# Lookup Apple
print(cusip_lookup['037833100'])

# Closing price for day before
closing_price_date = datetime(2019, 8, 2)
alphabet_hist = {datetime(2019, 8, 2, 0, 0): 1196.32, datetime(2019, 8, 1, 0, 0): 1211.78, datetime(2019, 7, 31, 0, 0): 1218.2, datetime(2019, 7, 30, 0, 0): 1228}

day_before_closing_price_date = closing_price_date - timedelta(days=1)

# Safely print closing price day before or None if it's missing
print(alphabet_hist.get(day_before_closing_price_date))

# Print with key
print(alphabet_hist)

# Remove entry
del(alphabet_hist[closing_price_date])

# Print with key deleted
print(alphabet_hist)

# Assign a value to cash.
cash = 19.11
non_cash = 20.33

# Check if cash is equal to non-cash
print(cash == non_cash)

# Assign the value of cash to be equal non-cash
cash = non_cash

# Check if cash is equal to non-cash
print(cash == non_cash)

# Check dividend is greater than zero
d1 = 323
d2 = 489
print(d2 > 0)

# Is dividend 1 is greater than dividend 2?
print(d1 > d2)

# Check dividend 1 is at least 100
print(d1 >= 100)

# Check dividend 2 is at least as much dividend 1
print(d1 <= d2)

# Print the given variables
is_investment_account = True
balance_positive = True
print(is_investment_account)
print(balance_positive)

# Decide if this account is cantidate for trading advice
potential_trade = is_investment_account and balance_positive

# Print if this represents a potential trade
print(potential_trade)

# Assign a default action if no input
input_action = ''
is_trading_day = False
action = input_action or "Hold"

# Print the action
print(action)

# Assign action only if trades can be made
do_action = is_trading_day and action

# Print the action to do
print(do_action)

closing_prices = []
market_closed = False
print(closing_prices)

# Assigning True if we need to get the prices
not_prices = not closing_prices

print(not_prices)

# Get prices if market is closed and we don't have prices
get_prices = not (market_closed and not_prices)

print(get_prices)

purchases = []
sales = []

# Get number of purchases
num_purchases = len(purchases)
# Get number of sales
num_sales = len(sales)

# Check if more sales than purchases
if num_purchases < num_sales:
    print('buy more')

# Check if fewer sales than purchases
if num_sales < num_purchases:
    print('sell more')

# Check if both lists are empty
if not (purchases or sales):
    print('No sales or purchases')

appl = []
tsla = []
amzn = []
trn = {'symbol': 'APPL', 'amount': 300, 'type': 'DIVIDEND'}
# Get the symbol value
symbol = trn['symbol']

# Check if Apple stock
if symbol == 'APPL':
    appl.append(trn)
# Check if Tesla stock
elif symbol == 'TSLA':
    tsla.append(trn)
# Check if Amazon stock
elif symbol == 'AMZN':
    amzn.append(trn)
# Handle other companies
else:
    print(symbol)

buy = {'symbol': 'CSCO', 'total_cost': 200}
buys = [{'symbol': 'AAPL', 'total_cost': 900}, {'symbol': 'ORCL', 'total_cost': 300}, {'symbol': 'CSCO', 'total_cost': 200}]
balance = 1299

# Loop through buys
for buy in buys:
    print('Buying ' + buy['symbol'])
    new_balance = balance - buy['total_cost']
    if new_balance < 0:
        print('Unable to finish buys')
        break
    balance = new_balance

print(balance)

nea = {datetime(1929, 1, 1, 0, 0): 0.38299999999999995, datetime(1930, 1, 1, 0, 0): 0.32299999999999995, datetime(1931, 1, 1, 0, 0): 0.001, datetime(1932, 1, 1, 0, 0): 0.043, datetime(1933, 1, 1, 0, 0): 0.057999999999999996, datetime(1934, 1, 1, 0, 0): 0.322, datetime(1935, 1, 1, 0, 0): -0.213, datetime(1936, 1, 1, 0, 0): -0.147, datetime(1937, 1, 1, 0, 0): 0.078, datetime(1938, 1, 1, 0, 0): 0.966, datetime(1939, 1, 1, 0, 0): 0.833, datetime(1940, 1, 1, 0, 0): 1.4709999999999999, datetime(1941, 1, 1, 0, 0): 1.033, datetime(1942, 1, 1, 0, 0): -0.252, datetime(1943, 1, 1, 0, 0): -2.246, datetime(1944, 1, 1, 0, 0): -2.024, datetime(1945, 1, 1, 0, 0): -0.7659999999999999, datetime(1946, 1, 1, 0, 0): 7.182, datetime(1947, 1, 1, 0, 0): 10.807, datetime(1948, 1, 1, 0, 0): 5.487, datetime(1949, 1, 1, 0, 0): 5.235, datetime(1950, 1, 1, 0, 0): 0.738, datetime(1951, 1, 1, 0, 0): 2.513, datetime(1952, 1, 1, 0, 0): 1.1640000000000001, datetime(1953, 1, 1, 0, 0): -0.701, datetime(1954, 1, 1, 0, 0): 0.40399999999999997, datetime(1955, 1, 1, 0, 0): 0.478, datetime(1956, 1, 1, 0, 0): 2.3609999999999998, datetime(1957, 1, 1, 0, 0): 4.075, datetime(1958, 1, 1, 0, 0): 0.5379999999999999, datetime(1959, 1, 1, 0, 0): 0.397, datetime(1960, 1, 1, 0, 0): 4.204, datetime(1961, 1, 1, 0, 0): 4.914, datetime(1962, 1, 1, 0, 0): 4.101, datetime(1963, 1, 1, 0, 0): 4.939, datetime(1964, 1, 1, 0, 0): 6.915, datetime(1965, 1, 1, 0, 0): 5.617999999999999, datetime(1966, 1, 1, 0, 0): 3.863, datetime(1967, 1, 1, 0, 0): 3.555, datetime(1968, 1, 1, 0, 0): 1.35, datetime(1969, 1, 1, 0, 0): 1.431, datetime(1970, 1, 1, 0, 0): 3.948, datetime(1971, 1, 1, 0, 0): 0.621, datetime(1972, 1, 1, 0, 0): -3.373, datetime(1973, 1, 1, 0, 0): 4.111000000000001, datetime(1974, 1, 1, 0, 0): -0.815, datetime(1975, 1, 1, 0, 0): 15.977, datetime(1976, 1, 1, 0, 0): -1.631, datetime(1977, 1, 1, 0, 0): -23.094, datetime(1978, 1, 1, 0, 0): -25.366, datetime(1979, 1, 1, 0, 0): -22.545, datetime(1980, 1, 1, 0, 0): -13.056, datetime(1981, 1, 1, 0, 0): -12.519, datetime(1982, 1, 1, 0, 0): -19.974, datetime(1983, 1, 1, 0, 0): -51.641999999999996, datetime(1984, 1, 1, 0, 0): -102.727, datetime(1985, 1, 1, 0, 0): -114.01799999999999, datetime(1986, 1, 1, 0, 0): -131.869, datetime(1987, 1, 1, 0, 0): -144.77, datetime(1988, 1, 1, 0, 0): -109.39299999999999, datetime(1989, 1, 1, 0, 0): -86.741, datetime(1990, 1, 1, 0, 0): -77.855, datetime(1991, 1, 1, 0, 0): -28.614, datetime(1992, 1, 1, 0, 0): -34.738, datetime(1993, 1, 1, 0, 0): -65.173, datetime(1994, 1, 1, 0, 0): -92.48700000000001, datetime(1995, 1, 1, 0, 0): -89.76100000000001, datetime(1996, 1, 1, 0, 0): -96.376, datetime(1997, 1, 1, 0, 0): -101.971, datetime(1998, 1, 1, 0, 0): -162.711, datetime(1999, 1, 1, 0, 0): -255.834, datetime(2000, 1, 1, 0, 0): -375.05, datetime(2001, 1, 1, 0, 0): -367.92900000000003, datetime(2002, 1, 1, 0, 0): -425.402, datetime(2003, 1, 1, 0, 0): -503.12699999999995, datetime(2004, 1, 1, 0, 0): -619.075, datetime(2005, 1, 1, 0, 0): -721.193, datetime(2006, 1, 1, 0, 0): -770.924, datetime(2007, 1, 1, 0, 0): -718.426, datetime(2008, 1, 1, 0, 0): -723.0880000000001, datetime(2009, 1, 1, 0, 0): -396.45099999999996, datetime(2010, 1, 1, 0, 0): -513.903, datetime(2011, 1, 1, 0, 0): -579.462, datetime(2012, 1, 1, 0, 0): -568.571, datetime(2013, 1, 1, 0, 0): -490.782, datetime(2014, 1, 1, 0, 0): -507.658, datetime(2015, 1, 1, 0, 0): -519.845, datetime(2016, 1, 1, 0, 0): -518.807, datetime(2017, 1, 1, 0, 0): -575.336, datetime(2018, 1, 1, 0, 0): -638.214}
surplus_years = []
query_date = datetime(2008, 1, 1)

# Loop while true
while True:
    net_exports = nea.get(query_date, -1)
    query_date = datetime(query_date.year - 1, 1, 1)
    # Skip if net exports are not positive
    if net_exports < 0:
           continue
    surplus_years.append(query_date)
    # Check if 5 years have been collected
    if len(surplus_years) == 5:
        # Stop the loop
        break
print(surplus_years)

import pandas as pd

# Create dict holding the data
data = {'Sym': ['APPL', 'APPL', 'APPL'],
        'Price': [105.00, 117.05, 289.80],
        'Date': ['2015/12/31', '2017/12/01', '2019/12/27']}

# Create DataFrame from the data
positions = pd.DataFrame(data=data)
print(positions)

# Make list of dictionaries
data = [{'Sym': 'APPL', 'Price': 105.00, 'Date': '2015/12/31'},
        {'Sym': 'APPL', 'Price': 117.05, 'Date': '2017/12/01'},
        {'Sym': 'APPL', 'Price': 289.80, 'Date': '2019/12/27'}]

# Create DataFrame from the list
positions = pd.DataFrame(data=data)
print(positions)

# Create a list of lists
data = [['APPL', 105.00, '2015/12/31'],
        ['APPL', 117.05, '2017/12/01'],
        ['APPL', 289.80, '2019/12/27']]

# Define the column names
columns = ['Sym', 'Price', 'Date']

# Create a DataFrame with the data and column names
df = pd.DataFrame(data=data, columns=columns)
print(df)

# Read the data
stocks = pd.read_csv('HistoricalQuotes.csv')

# Look at the data
print(stocks)

# Read the data
ledger = pd.read_csv('LedgerM2.csv', index_col=0)
ledger.index = ledger.index.astype(str)

# Look at the data
print(ledger)

# All columns for October 1st
print(ledger.loc['01/10/2020', :])

# Balance for all dates
print(ledger.loc[:, 'Balance'])

# Cell first row, Balance column
print(ledger.iloc[[0], [2]])

# Cell last row, Cash column
print(ledger.iloc[[2], [0]])

# Oldest two Securites amounts
print(ledger.iloc[0:2, 1])

# Newest Securites and Balance
print(ledger.iloc[2, 1:3])

# Set October 2nd Cash quantity
ledger.iloc[1, 0] = 1500

print(ledger)

# Set Balance of all to 2000
ledger.iloc[0:, 2] = 2000

print(ledger)

# Peak at top five rows
alphabet = pd.read_csv('HistoricalQuotes.csv', index_col=0)
alphabet.drop(['13:33'], inplace=True)
print(alphabet.head())
print(alphabet.tail(1))

print(alphabet.describe())
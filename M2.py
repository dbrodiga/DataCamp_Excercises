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


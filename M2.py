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
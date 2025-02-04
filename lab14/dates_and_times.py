from datetime import datetime, timedelta

# Getting the Current Date and Time

current_time = datetime.now()
print("Current date and time:", current_time)   

# Extracting Specific Parts of a Date

print ("Year:", current_time.year)
print ("Month:", current_time.month)
print ("Day:", current_time.day)
print ("Hour:", current_time.hour)
print ("Minute:", current_time.minute)
print ("Second:", current_time.second)

# Creating a Specific Date and Time

specific_date = datetime(2023, 12, 25, 10, 30, 0)
print("Specific Date:", specific_date)

# Formatting Dates and Times (strftime)

formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# Parsing Strings into Date Objects (strptime)

date_str = "01-02-2025 14:30:45"
date_obj = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
print("Parsed Date Object:", date_obj)

# Performing Date Calculations (timedelta)

future_date = current_time + timedelta(days=7)
print("Future Date:", future_date)

past_date = current_time - timedelta(days=3)
print("Past Date:", past_date)

# Finding the Difference Between Two Dates

event_date = datetime(2025, 12, 31)
days_remaining = event_date - current_time
print("Days until")
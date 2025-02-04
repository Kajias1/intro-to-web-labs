# Calculating the Difference Between Two Dates

from datetime import datetime

current_date = datetime.now()
future_date = datetime(2025, 6, 1)

timedelta = future_date - current_date

print(f"Days remaining before {future_date.strftime("%d %h %Y")}:", timedelta.days, "days")
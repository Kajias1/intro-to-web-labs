# Displaying the Current Date and Time

from datetime import datetime

now = datetime.now()

formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", formatted_now)
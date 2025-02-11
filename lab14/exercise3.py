import time
from datetime import datetime, timedelta

def countdown_timer(seconds):
    end_time = datetime.now() + timedelta(seconds=seconds)
    while True:
        remaining = end_time - datetime.now()
        total_seconds = int(remaining.total_seconds())

        if total_seconds <= 0:
            print("Time remaining: 0 seconds")
            break
        
        print(f"Time remaining: {total_seconds} seconds", end="\r")
        time.sleep(1)
    print("\nTimer finished!")


countdown_timer(10)
import time
from datetime import datetime

def print_date_every_second():
    try:
        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(current_time)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user.")


print_date_every_second()

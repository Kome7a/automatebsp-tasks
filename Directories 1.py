import os
from datetime import datetime


def file_time_created(path):
    timestamp = os.path.getctime(path)
    formatted = datetime.fromtimestamp(timestamp).strftime("on %Y-%m-%d at %H:%M")
    return formatted


result = file_time_created(r"C:\Users\ACER\Pictures\Screenshots")
print(result)

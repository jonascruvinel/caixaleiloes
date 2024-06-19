
import os
import datetime

def get_file_modification_date(file_path):
    modification_time = os.path.getmtime(file_path)
    modification_date = datetime.datetime.fromtimestamp(modification_time)
    return modification_date

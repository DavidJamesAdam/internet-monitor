import csv
from datetime import *
import speedtest
import time

import visualize


def user_interval():
    """[summary] add delay

    Returns:
        t_interval
        [type]: [description]
    """
    while True:
        try:
            s = int(input("Enter an interval to test for (minutes): "))
            return s * 60
        except ValueError:
            print("Invalid input. Please enter a valid number of minutes: ")


def runtime():
    """[summary] 

    Returns:
        t_end
        [type]: [description]
    """
    while True:
        try:
            r = int(input("How long do you want the test to run for (minutes): "))
            return r
        except ValueError:
            print("Invalid input. Please enter a valid number of minutes: ")


t_interval = user_interval()
t_end = datetime.now() + timedelta(minutes=(runtime()))

# TODO: Check connection before starting operation.
# import requests...
# url = "http://www.kite.com"
# timeout = 5
# try:
#     request = requests.get(url, timeout=timeout)
#     print("Connected to the Internet")
# except (requests.ConnectionError, requests.Timeout) as exception:
#     print("No internet connection.")

# print("Connection established successfully."
#     "\nComputing your internet speeds...."
#     "\nPress ctrl+c to exit")

st = speedtest.Speedtest()
time_format = "%H:%M"
date_now = datetime.now().strftime('%Y-%m-%d')

# TODO: get os to mkdir ` os.mkdir(path[, mode]) `

# os.mkdir `Output` (if not already exsisit)
# os.mkdir `cache`


with open(f"Cache/{date_now}.csv", mode='w') as speedtestcsv:
    write_csv = csv.DictWriter(speedtestcsv, fieldnames=[
        'Time', 'Download Speed', 'Upload Speed'])
    write_csv.writeheader()
    while True:
        if datetime.now() >= t_end:
            break
        else:
            current_time = datetime.now().strftime(time_format)
            # convert to mb/s
            download = round((round(st.download()) / 1048576), 2)
            upload = round((round(st.upload()) / 1048576), 2)
            print(
                f"Time: {current_time}, Download Speed: {download} Mb/s, Upload Speed: {upload} Mb/s")
            write_csv.writerow({'Time': current_time,
                                'Download Speed': download,
                                'Upload Speed': upload})
            time.sleep(t_interval)

visualize.visualize()

# os.delete /cache

print(f"Operation complete. Please check ---insert os path here--- for your results")
# TODO: put os.path in here.
# NOTE: How about just delete the csv when done -

raise SystemExit

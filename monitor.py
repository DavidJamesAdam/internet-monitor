import csv
from datetime import *
import speedtest
import time

s = speedtest.Speedtest()


def user_input():
    while True:
        try:
            s = int(input("Enter an interval to test for (minutes): "))
            return s * 60
        except ValueError:
            print("Invalid input. Please enter a valid number of minutes: ")


t_interval = user_input()
print("Computing your internet speeds.\nPress ctrl+c to exit")

time_format = "%H:%M"
date_now = datetime.now().strftime("%d-%m-%Y")


with open(f"Output/{date_now}.csv", mode='w') as speedtestcsv:
    write_csv = csv.DictWriter(speedtestcsv, fieldnames=[
        'Time', 'Download Speed', 'Upload Speed'])
    write_csv.writeheader()
    while True:
        current_time = datetime.now().strftime(time_format)
        download = round((round(s.download()) / 1048576), 2)
        upload = round((round(s.upload()) / 1048576), 2)
        print(
            f"Time: {current_time}, Download Speed: {download} Mb/s, Upload Speed: {upload} Mb/s")
        write_csv.writerow({'Time': current_time,
                            'Download Speed': download,
                            'Upload Speed': upload})
        time.sleep(t_interval)

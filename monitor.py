import csv
from datetime import *
import speedtest
import time


def user_interval():
    while True:
        try:
            s = int(input("Enter an interval to test for (minutes): "))
            return s * 60
        except ValueError:
            print("Invalid input. Please enter a valid number of minutes: ")


t_interval = user_interval()


def runtime():
    while True:
        try:
            r = int(input("How long do you want the test to run for (minutes): "))
            return r
        except ValueError:
            print("Invalid input. Please enter a valid number of minutes: ")


t_end = datetime.now() + timedelta(minutes=(runtime()))
# NOTE: class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

print("Computing your internet speeds.\nPress ctrl+c to exit")

st = speedtest.Speedtest()
time_format = "%H:%M"
date_now = datetime.now().strftime('%Y-%m-%d')

# TODO: get os to mkdir ` os.mkdir(path[, mode]) `

with open(f"Output/{date_now}.csv", mode='w') as speedtestcsv:
    write_csv = csv.DictWriter(speedtestcsv, fieldnames=[
        'Time', 'Download Speed', 'Upload Speed'])
    write_csv.writeheader()
    while True:
        if datetime.now() >= t_end:
            break
        else:
            current_time = datetime.now().strftime(time_format)
            download = round((round(st.download()) / 1048576), 2)
            upload = round((round(st.upload()) / 1048576), 2)
            print(
                f"Time: {current_time}, Download Speed: {download} Mb/s, Upload Speed: {upload} Mb/s")
            write_csv.writerow({'Time': current_time,
                                'Download Speed': download,
                                'Upload Speed': upload})
            time.sleep(t_interval)


raise SystemExit

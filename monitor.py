import csv
from datetime import datetime
import os
import requests
import shutil
import speedtest
import time
import functions
import visualize

# Check connection before starting operation.
try:
    request = requests.get("https://www.speedtest.net", timeout=5)
    print("\nConnection established successfully")
except (requests.ConnectionError, requests.Timeout) as exception:
    print("Connection failed. Please check your internet connection")
    raise SystemExit

time.sleep(1)
print("Computing your internet speeds....")
time.sleep(0.5)
print("Press ctrl+c to kill process")

s = speedtest.Speedtest()
time_format = "%H:%M:%S"
date_now = datetime.now().strftime('%Y-%m-%d')
end_time = functions.end_time()

# Create cache directory if it doesn't exist
if not os.path.exists('cache'):
    os.mkdir('cache')

with open(f"cache/{date_now}.csv", mode='w') as speedtestcsv:
    write_csv = csv.DictWriter(speedtestcsv, fieldnames=[
        'Time', 'Download Speed', 'Upload Speed'])
    write_csv.writeheader()

visualize.runGraph()
print("Monitor test")

while True:
    current_time = datetime.now().strftime(time_format)
    if current_time > end_time:
        break
    else:
        with open(f"cache/{date_now}.csv", mode='a') as speedtestcsv:
            write_csv = csv.DictWriter(speedtestcsv, fieldnames=[
                'Time', 'Download Speed', 'Upload Speed'])
            # convert to mb/s
            download = round((round(s.download()) / 1048576), 2)
            upload = round((round(s.upload()) / 1048576), 2)
            print(
                f"Time: {current_time}, Download Speed: {download} Mb/s, Upload Speed: {upload} Mb/s")
            write_csv.writerow({'Time': current_time,
                                'Download Speed': download,
                                'Upload Speed': upload})

# Clear cache
shutil.rmtree('cache')

print("Monitoring complete")

raise SystemExit

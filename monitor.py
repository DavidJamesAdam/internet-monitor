import csv
import datetime
import speedtest
import time

s = speedtest.Speedtest()
# delay = 60
time_format = "%H:%M:%S"

with open('test.csv', mode='w') as speedtestcsv:
    write_csv = csv.DictWriter(speedtestcsv, fieldnames=[
        'Time', 'Download Speed', 'Upload Speed'])
    write_csv.writeheader()
    while True:
        current_time = datetime.datetime.now().strftime(time_format)
        download = round((round(s.download()) / 1048576), 2)
        upload = round((round(s.upload()) / 1048576), 2)
        print(
            f"Time: {current_time}, Download Speed: {download} Mb/s, Upload Speed: {upload} Mb/s")
        write_csv.writerow({'Time': current_time,
                            'Download Speed': download,
                            'Upload Speed': upload})
        # time.sleep(delay)

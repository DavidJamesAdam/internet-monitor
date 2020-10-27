import datetime
import speedtest
import time

s = speedtest.Speedtest()

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    download = round((round(s.download()) / 1048576), 2)
    upload = round((round(s.upload()) / 1048576), 2)

    print(
        f"time: {current_time}, Download Speed: {download}Mb/s, Upload Speed: {upload}Mb/s")

    time.sleep(60)

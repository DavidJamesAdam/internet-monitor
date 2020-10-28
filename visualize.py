import csv
from datetime import datetime
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


times = []
download = []
upload = []

date_now = datetime.now().strftime('%Y-%m-%d')
# TODO:  get this to read from monitor.py


with open(f"Output/2020-10-27.csv", 'r') as csvfile:    # date_now fileaname
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        times.append(str(row[0]))
        download.append(float(row[1]))
        upload.append(float(row[2]))

print(times, "\n", download, "\n", upload)

# matplotlib
plt.figure(50)
plt.plot(times, download, label='Download Speed', color='r')
plt.plot(times, upload, label='Upload Speed', color='g')
plt.xlabel('Time')      # How to make this more ligible????
plt.ylabel('Speed (Mb/s)')
plt.title(f"Internet Speed {date_now}")
plt.legend()
plt.savefig('test_graph.jpg', bbox_inches='tight')

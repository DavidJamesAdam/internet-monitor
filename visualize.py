import csv
from datetime import datetime
import matplotlib.pyplot as plt
import os

"""[summary]
"""
times = []
download = []
upload = []
date_now = datetime.now().strftime('%Y-%m-%d')

if not os.path.exists('Output'):
    os.mkdir('Output')
# else:
#     pass


def visualize():
    """[summary]
    """
    with open(f"Cache/{date_now}.csv", 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in plots:
            times.append(str(row[0]))
            download.append(float(row[1]))
            upload.append(float(row[2]))

    # matplotlib
    # plt.figure(100)
    w = 20
    h = 10
    d = 300
    plt.figure(figsize=(w, h), dpi=d)
    plt.plot(times, download, label='Download Speed', color='r')
    plt.plot(times, upload, label='Upload Speed', color='g')
    plt.xlabel('Time')
    plt.ylabel('Speed (Mb/s)')
    plt.xticks(rotation=45)
    plt.title(f"Internet Speed {date_now}")
    plt.legend()
    plt.savefig(f"Output/{date_now}.jpg", bbox_inches='tight')

    # delete cache here??

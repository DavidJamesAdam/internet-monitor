import csv
from datetime import datetime
import os
import time
import speedtest
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas
import keyboard

# Initialize variables
times = []
download = []
upload = []
date_now = datetime.now().strftime('%Y-%m-%d')
time_format = "%H:%M:%S"

# Create cache directory if it doesn't exist
if not os.path.exists('cache'):
    os.mkdir('cache')

# Function to monitor internet speed and save to CSV
def monitor():
    s = speedtest.Speedtest()
    with open(f"cache/{date_now}.csv", mode='w') as speedtestcsv:
        write_csv = csv.DictWriter(speedtestcsv, fieldnames=[
            'Time', 'Download Speed', 'Upload Speed'])
        write_csv.writeheader()
        while True:
            if keyboard.is_pressed('q'):
                break
            else:
                current_time = datetime.now().strftime(time_format)
                # Convert to mb/s
                download_speed = round((round(s.download()) / 1048576), 2)
                upload_speed = round((round(s.upload()) / 1048576), 2)
                print(
                    f"Time: {current_time}, Download Speed: {download_speed} Mb/s, Upload Speed: {upload_speed} Mb/s")
                write_csv.writerow({'Time': current_time,
                                    'Download Speed': download_speed,
                                    'Upload Speed': upload_speed})
                time.sleep(1)  # Adjust the interval as needed

# Function to visualize the data
def visualize(i):
    data = pandas.read_csv(f'cache/{date_now}.csv')
    x = data['Time']
    y1 = data['Download Speed']
    y2 = data['Upload Speed']
    plt.cla()

    plt.plot(x, y1, label='Download Speed')
    plt.plot(x, y2, label='Upload Speed')
    plt.xticks(rotation=90)

    plt.legend(loc='upper left')
    plt.tight_layout()

    # Annotate each point with its value
    for j in range(len(x)):
        plt.annotate(f'{y1[j]}', (x[j], y1[j]), textcoords="offset points", xytext=(0,10), ha='center')
        plt.annotate(f'{y2[j]}', (x[j], y2[j]), textcoords="offset points", xytext=(0,10), ha='center')

# Main function to run monitoring and visualization
def main():
    print("Computing your internet speeds....")
    time.sleep(0.5)
    print("Press Q to stop and gather data\nPress ctrl+c to kill process")

    monitor()

    liveGraph = FuncAnimation(plt.gcf(), visualize, interval=1000, cache_frame_data=False)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
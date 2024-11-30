from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas

times = []
download = []
upload = []
date_now = datetime.now().strftime('%Y-%m-%d')


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

liveGraph = FuncAnimation(plt.gcf(), visualize, interval=1000, cache_frame_data=False)

plt.tight_layout()
plt.show()

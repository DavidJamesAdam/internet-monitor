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

    for j in range(len(x)):
        plt.annotate(f'{y1[j]}', (x[j], y1[j]), textcoords="offset points", xytext=(0,10), ha='center')
        plt.annotate(f'{y2[j]}', (x[j], y2[j]), textcoords="offset points", xytext=(0,10), ha='center')

liveGraph = FuncAnimation(plt.gcf(), visualize, interval=1000, cache_frame_data=False)

def runGraph():
    liveGraph

    plt.tight_layout()
    plt.show()

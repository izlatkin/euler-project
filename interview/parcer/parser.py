from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib
import numpy as np
import time
from matplotlib.ticker import FuncFormatter

def read_log():
    lines = open('log2.txt', 'r').readlines()
    results = []
    for line in lines:
        if 'rq_t' in line:
            tmp = line.strip().split()[5]
            results.append(tmp)
    return results

def plot_ts(times):
    values = [t - times[i] for i, t in enumerate(times[1:])]
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=25)
    ax = plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    plt.plot(np.array(times), np.array(times))
    plt.show()


def format_func(x, pos):
    hours = int(x//3600)
    minutes = int((x%3600)//60)
    seconds = int(x%60)
    return "{:d}:{:02d}".format(hours, minutes)

def plot_ts2(times):
    labels = range(len(times) - 1)
    values = [t - times[i] for i, t in enumerate(times[1:])]
    seconds = [i.seconds for i in values]
    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)
    ax.bar(labels, seconds)
    formatter = FuncFormatter(format_func)
    ax.yaxis.set_major_formatter(formatter)
    # this locates y-ticks at the hours
    ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=3600))
    # this ensures each bar has a 'date' label
    ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=1))
    plt.show()

def plot_ts3(times):
    result = [(t - times[i]).total_seconds() for i, t in enumerate(times[1:])]
    x = range(1, len(result) + 1)
    plt.clf()
    plt.plot(x, result)
    plt.xlabel("x - iteration")
    plt.ylabel('y - todos')
    plt.title('iteration progress')
    plt.show()
    #plt.savefig(dir + '/iteration_progress.png')

def main():
    times = read_log()
    print(times)
    plot_ts3([datetime.strptime(t, "%H:%M:%S") for t in times])
    # for t in times:
    #     mytime = datetime.strptime(t, "%H:%M:%S")
    #     print(mytime)



if __name__ == '__main__':
    main()
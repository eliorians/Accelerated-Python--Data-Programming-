import pandas as pd
import matplotlib.pyplot as plt
from time import time
from random import randint

def file_bmi(filename):

    #from csv
    df = pd.read_csv(filename)
    h = list(df['Height'])
    w = list(df['Weight'])
    
    #calculations
    bmi = []
    for i in range(0, len(w)):
        bmi.append((w[i] * 703)/(h[i] * h[i]))
    
    #to csv
    df['BMI'] = bmi
    filename = filename[:len(filename)-4] + "_bmi" + filename[len(filename)-4:]
    df.to_csv(filename, index = False)

def plot_signals(filename):

    #from csv
    df = pd.read_csv(filename)
    columnNames = list(df.columns)
    x = list(df[columnNames[0]])
    y1 = list(df[columnNames[1]])
    y2 = list(df[columnNames[2]])
    y3 = list(df[columnNames[3]])

    filename = filename[:len(filename)-4] + "_plot.png"

    #plot x,y1 x,y2 and x, with specified styles
    plt.plot(x, y1, label = columnNames[1], color = 'green', marker = 'o', linestyle = '--', linewidth = 2)
    plt.plot(x, y2, label = columnNames[2], color = 'cyan', marker = 'p', linestyle = ':', linewidth = 2)
    plt.plot(x, y3, label = columnNames[3], color = 'orange', marker = 'D', linestyle = '-.', linewidth = 2)

    #labels
    plt.legend()
    plt.title(filename)
    plt.xlabel('time')
    plt.ylabel('amplitude')

    #return
    plt.savefig(filename)


def grade_histogram(filename):

    #from csv
    df = pd.read_csv(filename)
    filename = filename[:len(filename)-4] + "_hist.png"

    #calculations
    x = list(df['Grades'])

    #labels and style
    plt.hist(x, bins = range(0,101, 5), facecolor = 'cyan', edgecolor = 'black', hatch = '/')
    plt.xlabel('Grades')
    plt.ylabel('Count')
    plt.title(filename)
    #diagonal hatching

    #return
    plt.savefig(filename)
    plt.show()

def time_it(a, n, value):
    avg = 0
    for i in range(n):
        t0 = time()
        for j in range(len(a)):
            if (j == value):
                t1 = time()
                avg = avg + (t1-t0)

    return (avg / n)
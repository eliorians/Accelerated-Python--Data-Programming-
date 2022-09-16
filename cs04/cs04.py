
def get_times(num_samples, start_time, sample_rate):
    x = []
    for i in range(0, num_samples):
        x.append(start_time+i/sample_rate)
    return x

def scale(y, alpha):
    return [i * alpha for i in y]

def clip(y):
    for i in range(0, len(y)):
        if (y[i] > 32767):
            y[i] = 32767
        if (y[i] < -32768):
            y[i] = -32768
    return y

def zoom(x, y, start, stop):
    return x[start:stop], y[start:stop]

def double_pitch(y):
    return y[::2]

def half_pitch(y):
    return [i for i in y for _ in (0, 1)]

def plot_audio(x, y, title):
    import matplotlib.pyplot as plt

    plt.plot(x, y)
    plt.title(title)  
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')

    filename = title + '.png'
    plt.savefig(filename)
    return plt
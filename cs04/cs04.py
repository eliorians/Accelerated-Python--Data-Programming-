
def get_times(num_samples, start_time, sample_rate):
    x = []
    for i in range(start_time, num_samples):
        x.append(i/sample_rate)
    return x

def scale(y, alpha):
    return [i * alpha for i in y]

def clip(y):
    new_y = []
    for i in range(0, len(y)):
        if (new_y[i] > 32767):
            new_y[i] = 32767
        if (new_y[i] < -32768):
            new_y[i] = -32768
    return new_y

def zoom(x, y, start, stop):
    return x[start:stop], y[start:stop]

def double_pitch(y):
    return y[::2]

def half_pitch(y):
    return [i for i in y for _ in (0, 1)]

def plot_audio(x, y, title):
    import matplotlib.pyplot as plt
    from audio_helpers import save

    plt.plot(x, y)
    plt.title(title)  
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')

    plt.savefig(title++"png")
    return plt

from audio_helpers import load
rate, data = load('speech.wav')
plt = plot_audio(range(len(data)), data, 'Wrong Times')
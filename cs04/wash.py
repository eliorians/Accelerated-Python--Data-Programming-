from audio_helpers import load, save
import matplotlib.pyplot as plt
import cs04

rate, data = load('speech.wav')
time = cs04.get_times(len(data), data[0]/rate, rate)
time, data = cs04.zoom(time, data, 87300, 87450)
data = cs04.scale(data, 5)
data = cs04.clip(data)
save('wash.wav', rate, data)
rate, data = load('wash.wav')
plt = cs04.plot_audio(range(len(data)), data, 'wash')
plt.show()

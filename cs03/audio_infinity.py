from audio_helpers import load, save
import matplotlib.pyplot as plt

file_name = input("Enter the WAV file name: ")
rate, data = load(file_name)

#scale the data by a big number
data = [i * 100000 for i in data]
#clip the range
for i in range(0, len(data)):
    if (data[i] > 32767):
        data[i] = 32767
    if (data[i] < -32768):
        data[i] = -32768

print(f'The clipped range is ({min(data)}, {max(data)}).')
file_name = file_name[:len(file_name)-4] + "_infinity" + file_name[len(file_name)-4:]
save(file_name, rate, data)

x = [0]
for i in range(1, len(data)):
    x.append(i/rate)
y = data
plt.plot(x, y)
plt.xlabel('Time (seconds)')
plt.title(file_name)
plt.show()
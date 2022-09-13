from audio_helpers import load, save
import matplotlib.pyplot as plt

file_name = input("Enter the WAV file name: ")
rate, data = load(file_name)
save('edited.wav', rate, data)

#scale the data by two
data = [i * 2 for i in data]
#clip the range
for i in range(0, len(data)):
    if (data[i] > 32767):
        data[i] = 32767
    if (data[i] < -32768):
        data[i] = -32768

print(f'The clipped range is ({min(data)}, {max(data)}).')

x = range(0, len(data))
y = data
plt.plot(x, y)
plt.xlabel('Time (seconds)')
plt.title(file_name)
plt.show()
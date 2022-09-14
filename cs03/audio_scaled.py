from audio_helpers import load, save
import matplotlib.pyplot as plt

file_name = input("Enter the WAV file name: ")
rate, data = load(file_name)

print(f'The original range is ({min(data)}, {max(data)}).')

#scale the data by two
data = [i * 2 for i in data]
save('speech_scaled.wav', rate, data)
print(f'The new range is ({min(data)}, {max(data)}).')

x = [0]
for i in range(1, len(data)):
    x.append(i/rate)
y = data
plt.plot(x, y)
plt.xlabel('Time (seconds)')
plt.title(file_name)
plt.show()
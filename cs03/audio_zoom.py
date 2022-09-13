from audio_helpers import load, save
import matplotlib.pyplot as plt

file_name = input("Enter the WAV file name: ")
rate, data = load(file_name)
save('edited.wav', rate, data)

#zoom / splice list
data = data[79000:97000]

print(f'The selected range is ({min(data)}, {max(data)}).')
print(f'There selection has {len(data)} samples.')
print(f'The selection is {len(data) / rate:.3f} seconds long.')
print(f'The selection starts at {79000/rate:.3f} and ends at {97000/rate:.3f}.')

x = range(0, len(data))
y = data
plt.plot(x, y)
plt.xlabel('Time (seconds)')
plt.title(file_name)
plt.show()
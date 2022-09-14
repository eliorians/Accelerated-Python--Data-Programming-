from audio_helpers import load, save
import matplotlib.pyplot as plt

file_name = input("Enter the WAV file name: ")
rate, data = load(file_name)

#zoom / splice list
data = data[79000:97000]

print(f'The selected range is ({min(data)}, {max(data)}).')
print(f'The selection has {len(data)} samples.')
print(f'The selection is {len(data) / rate:.3f} seconds long.')
print(f'The selection starts at {79000/rate:.3f} and ends at {97000/rate:.3f}.')

file_name = file_name[:len(file_name)-4] + "_zoom" + file_name[len(file_name)-4:]
save(file_name, rate, data)

x = []
for i in range(79000, 97000):
    x.append(i/rate)
y = data
plt.plot(x, y)
plt.xlabel('Time (seconds)')
plt.title(file_name)
plt.show()
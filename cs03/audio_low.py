from audio_helpers import load, save
import matplotlib.pyplot as plt

file_name = input("Enter the WAV file name: ")
rate, data = load(file_name)

#duplicate each element in list, lowering the pitch (same play rate)
data = [i for i in data for _ in (0, 1)]

print(f'The low audio has {len(data)} samples.')
print(f'The low audio is {len(data) / rate:.3f} seconds long.')

file_name = file_name[:len(file_name)-4] + "_clipped" + file_name[len(file_name)-4:]
save(file_name, rate, data)

x = range(0, len(data))
y = data
plt.plot(x, y)
plt.xlabel('Time (seconds)')
plt.title(file_name)    
plt.show()
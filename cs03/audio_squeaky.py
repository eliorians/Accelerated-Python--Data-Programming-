from audio_helpers import load, save
import matplotlib.pyplot as plt

file_name = input("Enter the WAV file name: ")
rate, data = load(file_name)
save('edited.wav', rate, data)

#zoom
data = data[::2]


print(f'The sqeaky audio has {len(data)} samples.')
print(f'The squeaky audio is {len(data) / rate:.3f} seconds long.')

x = range(0, len(data))
y = data
plt.plot(x, y)
plt.xlabel('Time (seconds)')
plt.title(file_name)    
plt.show()
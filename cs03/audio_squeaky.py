from audio_helpers import load, save
import matplotlib.pyplot as plt

file_name = input("Enter the WAV file name: ")
rate, data = load(file_name)

#cut number of elements in list in half - every other (making the audio high pitch w/ same play rate)
data = data[::2]

print(f'The sqeaky audio has {len(data)} samples.')
print(f'The squeaky audio is {len(data) / rate:.3f} seconds long.')

file_name = file_name[:len(file_name)-4] + "_squeaky" + file_name[len(file_name)-4:]
save(file_name, rate, data)

x = range(0, len(data))
y = data
plt.plot(x, y)
plt.xlabel('Time (seconds)')
plt.title(file_name)    
plt.show()
from audio_helpers import load, save
import matplotlib.pyplot as plt

#get filename
file_name = input("Enter the WAV file name: ")
#retrieve audio
rate, data = load(file_name)
#save audio
save('edited.wav', rate, data)

print(f'There are {len(data)} samples.')
print(f'The sample rate is {rate} samples/sec.')
print(f'The file is {len(data) / rate:.3f} seconds long.')

x = [len(data)/rate]
y = [data]
plt.plot(x, y)
plt.xlabel('Time (seconds)')
plt.title(file_name)
plt.show()
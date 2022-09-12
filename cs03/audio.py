from audio_helpers import load, save
import matplotlib.pyplot as plt

#get filename
file_name = input("Enter the WAV file name: ")
#retrieve audio
rate, data = load(file_name)
#save audio
data[0] = 0
save('edited.wav', rate, data)

x = [rate]
y = [data]
plt.plot(x,y)
plt.xlabel('Time (seconds)')
plt.ylabel('Sound Pressure')
plt.title(file_name)
plt.show

print(f'There are {data.len()} samples.')
print(f'The sample rate is {data.len() / rate.len()} samples/sec.')
print(f'The file is {rate.len():.3f} seconds long.')

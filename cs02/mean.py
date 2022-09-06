from random import random


num = int(input("Enter n: "))
total = 0
count = 0

while (count < num):
    total += random()
    count += 1

print(f'The average of {count} trials is {total/count:.3f}.')
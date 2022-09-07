from random import randint
wins = 0

for a in range(10):
    
    guess = int(input("What is your guess (1 or 2): "))
    coin = randint(1,2)

    if guess == coin:
        print(f'You are correct {guess} == {coin}.')
        wins += 1
    else:
        print(f'Sorry, {guess} != {coin}.')

print(f'You were correct {wins} times.')
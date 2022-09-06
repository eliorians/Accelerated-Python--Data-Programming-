from random import randint

guess = int(input("What is your guess (1 or 2): "))
coin = randint(1,2)

if guess == coin:
    print(f'You win! {guess} == {coin}')
else:
    print(f'You lose! {guess} != {coin}')
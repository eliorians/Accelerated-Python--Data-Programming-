num = int(input("Enter the score: "))
letter = ''

if (num > 100 or num < 0):
    letter = "invalid"
if (0 <= num < 60 ):
    letter = 'F'
if (60 <= num < 70 ):
    letter = 'D'
if (70 <= num < 80 ):
    letter = 'C'
if (80 <= num < 90 ):
    letter = 'B'
if (90 <= num <= 100 ):
    letter = 'A'

print(f'The score is {num:.1f} and the letter grade is {letter}.')
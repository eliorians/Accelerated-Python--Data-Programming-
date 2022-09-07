h = int(input("Enter height in inches: "))
w = int(input("Enter weight in pounds: "))

bmi = 703 * (w/(h**2))

if (bmi < 18.5):
    status = "underweight"
if (18.5 <= bmi < 25):
    status = "healthy"
if (25 <= bmi < 30):
    status = "overweight"
if (bmi >= 30):
    status = "obese"



print(f'The BMI is {bmi:.1f} which is considered to be {status}.')
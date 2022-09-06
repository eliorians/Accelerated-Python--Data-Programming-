sex = input("Enter sex (M or F): ")
fat = int(input("Enter the body fat percentage: "))

if ((sex == "M" and fat < 2) or (sex == "F" and fat < 10)):
    status = "Deficient"
if ((sex == "M" and 2 <= fat <= 5) or (sex == "F" and 10 <= fat <= 13)):
    status = "Essential fat"
if ((sex == "M" and 6 <= fat <= 13) or (sex == "F" and 14 <= fat <= 20)):
    status = "Athletes"
if ((sex == "M" and 14 <= fat <= 17) or (sex == "F" and 21 <= fat <= 24)):
    status = "Fitness"
if ((sex == "M" and 18 <= fat <= 24) or (sex == "F" and 25 <= fat <= 31)):
    status = "Average"
if ((sex == "M" and fat >= 25) or (sex == "F" and fat >= 32)):
    status = "Obese"

print(f'{fat:.1f}% body fat for a {sex} is considered {status}.')
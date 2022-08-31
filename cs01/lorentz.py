
c = 3e8
s = float(input("Enter the velocity (m/s): "))
result = 1/ ((1 - (s**2 / c**2))**(1/2))

print(f'The Lorentz factor at {s} is {result:.4f}.')
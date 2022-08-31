r1 = float(input("Enter r1: "))
r2 = float(input("Enter r2: "))
r3 = float(input("Enter r3: "))

rt = 1/ ((1/r1) + (1/r2) + (1/r3))

print(f'The parallel resistance of {r1}, {r2}, and {r3} ohms is {rt:.3f} ohms.')
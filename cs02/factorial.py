n = int(input("Enter n: "))
count = 1
product = 1

while count != n+1:
    print(f'{count} x {product} = {count * product}')
    
    product = count * product
    count += 1

print(f'{n}! = {product}')
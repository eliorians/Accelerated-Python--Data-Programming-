def gcd(m, n): 
    if n == 0: 
        return m 
    else: 
        return gcd(n, m % n) 


def gcd2(m, n):
 
    if m > n:
        small = n
    else:
        small = m
    for i in range(1, small + 1):
        if((m % i == 0) and (n % i == 0)):
            gcd = i
             
    return gcd
 

print(gcd2(30, 20))
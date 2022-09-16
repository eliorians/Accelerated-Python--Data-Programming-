var = 0

def test():   
    global var
    var = 1
    print(f'function var = {var}')

test()
print(f'global var = {var}')
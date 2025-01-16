num_1 = 210
num_2 = 45

def gcd(num_1, num_2):
    while num_2 != 0:
        
        rem = num_1 % num_2
        num_1 = num_2
        num_2 = rem

    return num_1

print(gcd(num_1, num_2))
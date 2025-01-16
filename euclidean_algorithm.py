num_1 = 210 #sets 2 variables for 2 numbers
num_2 = 45

def gcd(num_1, num_2):
    while num_2 != 0: #while the second number is not 0
        
        rem = num_1 % num_2 #gets the remainder of two numbers
        num_1 = num_2 #changes the first number as the second number
        num_2 = rem #changes the second number as the remainder
        #repeats process to find the greatest common divisor
    return num_1

print(gcd(num_1, num_2)) #prints the result
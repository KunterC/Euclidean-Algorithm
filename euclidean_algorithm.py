input_number_1 = int(input("Enter a number: "))
input_number_2 = int(input("Enter another number: "))

def greatest_common_divisor(num_1, num_2):
    while num_2 != 0: #while the second number is not 0
    
        num_1, num_2 = num_2, num_1 % num_2 #continuously sets first number as second 
                                            #and second as the remainder of the two numbers
    return num_1 #returns first number when second number is 0

gcd = greatest_common_divisor(input_number_1, input_number_2) #assigns a variable for the gcd.
print(f"The GCD of {input_number_1} and {input_number_2} is {gcd}.") #prints the result
while True:
    try:
        input_number_1 = int(input("Enter a number: ")) #gets the first user input and tests if they are integers
        input_number_2 = int(input("Enter another number: ")) #gets the second user input
        break #if input is valid it breaks the while loop
    except ValueError:
        print("Please enter numbers only.") #prints an error message when the input is not an integer
        continue #keeps prompting the user for valid input
    
def greatest_common_divisor(num_1, num_2):
    if num_1 < 0 or num_2 < 0: 
        return "Please enter positive numbers only." #if any number is negative it returns an error message
    
    while num_2 != 0: #while the second number is not 0
    
        num_1, num_2 = num_2, num_1 % num_2 #continuously sets first number as second 
                                            #and second as the remainder of the two numbers
    return f"The GCD of the numbers is {num_1}" #returns the GCD with a message

print(greatest_common_divisor(input_number_1, input_number_2)) #prints the function
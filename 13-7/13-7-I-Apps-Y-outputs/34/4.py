
def solve(x):
    # Convert x to a string
    x_str = str(x)
    
    # Get the first two digits of x
    first_two = x_str[:2]
    
    # Get the last five digits of x
    last_five = x_str[2:]
    
    # Convert the first two digits to an integer
    first_two_int = int(first_two)
    
    # Convert the last five digits to an integer
    last_five_int = int(last_five)
    
    # Calculate the sum of the first two digits and the last five digits
    sum = first_two_int + last_five_int
    
    # Calculate the difference of the first two digits and the last five digits
    diff = first_two_int - last_five_int
    
    # Return the two integers separated by a space
    return str(sum) + " " + str(diff)


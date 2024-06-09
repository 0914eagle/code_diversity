
def solve(x):
    # Convert x to a string
    x_str = str(x)
    
    # Get the first two digits of x
    first_two_digits = x_str[:2]
    
    # Get the last four digits of x
    last_four_digits = x_str[2:]
    
    # Convert the first two digits to an integer
    first_two_digits_int = int(first_two_digits)
    
    # Convert the last four digits to an integer
    last_four_digits_int = int(last_four_digits)
    
    # Calculate the sum of the first two digits and the last four digits
    sum = first_two_digits_int + last_four_digits_int
    
    # Calculate the difference of the first two digits and the last four digits
    difference = first_two_digits_int - last_four_digits_int
    
    # Calculate the product of the first two digits and the last four digits
    product = first_two_digits_int * last_four_digits_int
    
    # Return the sum, difference, and product as a list
    return [sum, difference, product]


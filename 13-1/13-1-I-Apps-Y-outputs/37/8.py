
def get_keypresses(x):
    # Convert the apartment number to a string
    x_str = str(x)
    
    # Initialize a counter for the total number of keypresses
    keypresses = 0
    
    # Iterate through each digit in the apartment number
    for digit in x_str:
        # Get the number of times the digit appears in the apartment number
        num_digits = x_str.count(digit)
        
        # Add the number of keypresses for the current digit
        keypresses += num_digits
    
    return keypresses


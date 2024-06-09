
def solve(remembered_substring, total_digits):
    # Initialize a list to store all possible numbers
    numbers = []
    
    # Loop through all possible numbers
    for i in range(10**(total_digits-len(remembered_substring))):
        # Convert the current number to a string
        number_string = str(i)
        
        # Pad the string with leading zeroes
        number_string = number_string.zfill(total_digits)
        
        # Check if the remembered substring is a substring of the current number string
        if remembered_substring in number_string:
            # Add the current number to the list of possible numbers
            numbers.append(int(number_string))
    
    # Return the smallest possible number
    return min(numbers)


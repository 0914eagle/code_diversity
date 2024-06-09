
def closest_handsome_number(n):
    # Convert the input number to a string
    n_str = str(n)
    
    # Initialize the closest handsome numbers as the input number itself
    closest_handsome_numbers = [n]
    
    # Iterate through the digits of the input number
    for i in range(len(n_str) - 1):
        # If the current digit and the next digit have different parity, add the next digit to the handsome number
        if n_str[i] % 2 != n_str[i+1] % 2:
            closest_handsome_numbers.append(int(n_str[:i+1] + n_str[i+1]))
    
    # Sort the handsome numbers in ascending order and return the closest two numbers
    return sorted(closest_handsome_numbers)


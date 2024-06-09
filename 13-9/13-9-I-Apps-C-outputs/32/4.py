
def get_closest_handsome_number(n):
    # Convert the input number to a string
    n_str = str(n)
    
    # Initialize the closest handsome numbers as the input number itself
    closest_handsome_numbers = [n]
    
    # Iterate through the digits of the input number
    for i in range(len(n_str) - 1):
        # Check if the current digit and the next digit have the same parity
        if int(n_str[i]) % 2 == int(n_str[i+1]) % 2:
            # If they have the same parity, replace the current digit with the next digit
            n_str = n_str[:i] + n_str[i+1] + n_str[i+2:]
    
    # Convert the modified string back to an integer
    closest_handsome_numbers.append(int(n_str))
    
    # Return the smallest handsome number
    return sorted(closest_handsome_numbers)[0]


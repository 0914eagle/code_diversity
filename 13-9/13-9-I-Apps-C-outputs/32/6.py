
def handsome_number(n):
    # Convert the input number to a string
    n_str = str(n)
    
    # Initialize the closest handsome number as the input number
    closest_handsome = n
    
    # Iterate through the digits of the input number
    for i in range(len(n_str) - 1):
        # Check if the current digit and the next digit have the same parity
        if int(n_str[i]) % 2 == int(n_str[i+1]) % 2:
            # If they have the same parity, find the closest handsome number by changing the parity of the current digit
            closest_handsome = int(n_str[:i] + str(int(n_str[i]) ^ 1) + n_str[i+1:])
            break
    
    return closest_handsome


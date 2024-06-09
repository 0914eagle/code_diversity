
def find_closest_handsome_number(n):
    # Convert the input number to a string
    n_str = str(n)
    
    # Initialize variables for the closest handsome numbers
    handsome_1 = 0
    handsome_2 = 0
    
    # Iterate through the digits of the input number
    for i in range(len(n_str) - 1):
        # Check if the current digit and the next digit have different parity
        if n_str[i] % 2 != n_str[i+1] % 2:
            # If they have different parity, check if the current digit is odd or even
            if n_str[i] % 2 == 1:
                # If the current digit is odd, the next digit must be even
                handsome_1 = int(n_str[i+1])
            else:
                # If the current digit is even, the next digit must be odd
                handsome_2 = int(n_str[i+1])
    
    # If both handsome numbers are found, return them in order
    if handsome_1 != 0 and handsome_2 != 0:
        return str(handsome_1) + " " + str(handsome_2)
    # If only one handsome number is found, return it
    elif handsome_1 != 0:
        return str(handsome_1)
    # If no handsome numbers are found, return 0
    else:
        return "0"


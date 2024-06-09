
def closest_handsome_number(n):
    # Convert the input number to a string
    n_str = str(n)
    
    # Initialize the closest handsome numbers as the input number itself
    handsome_numbers = [n]
    
    # Iterate through the digits of the input number
    for i in range(len(n_str) - 1):
        # If the current digit and the next digit have different parity, add the current digit to the handsome numbers
        if n_str[i] % 2 != n_str[i+1] % 2:
            handsome_numbers.append(int(n_str[i]))
    
    # Sort the handsome numbers in ascending order
    handsome_numbers.sort()
    
    # If there is only one handsome number, return it
    if len(handsome_numbers) == 1:
        return handsome_numbers[0]
    
    # If there are two handsome numbers, return the smaller one first and then the larger one
    return " ".join(str(handsome_numbers[0]), str(handsome_numbers[1]))


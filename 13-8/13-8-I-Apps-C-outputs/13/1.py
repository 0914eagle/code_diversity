
def get_divine_digits(n, k, a):
    # Initialize an empty list to store the divine digits
    divine_digits = []
    
    # Iterate over the banknote denominations
    for i in range(n):
        # Get the value of the current banknote
        value = a[i]
        
        # Find the remainder when the value is divided by the base
        remainder = value % k
        
        # If the remainder is a divine digit, add it to the list
        if remainder in divine_digits:
            divine_digits.append(remainder)
    
    # Return the list of divine digits
    return len(divine_digits), sorted(divine_digits)


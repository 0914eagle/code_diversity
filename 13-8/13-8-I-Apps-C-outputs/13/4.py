
def get_happy_digits(n, k, a):
    # Initialize a set to store the happy digits
    happy_digits = set()
    
    # Iterate over the banknote denominations
    for i in range(n):
        # Get the current denomination
        curr_denom = a[i]
        
        # Get the last digit of the current denomination in the Martian number system
        last_digit = curr_denom % k
        
        # If the last digit is a divine digit, add it to the set of happy digits
        if last_digit in [0, 4]:
            happy_digits.add(last_digit)
    
    # Return the number of happy digits and the set of happy digits
    return len(happy_digits), happy_digits


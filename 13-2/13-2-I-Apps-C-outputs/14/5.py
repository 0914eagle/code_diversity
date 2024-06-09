
def get_happy_digits(n, k, a):
    # Initialize a set to store the happy digits
    happy_digits = set()
    
    # Iterate over the banknote denominations
    for i in range(n):
        # Get the value of the current banknote
        value = a[i]
        
        # Iterate over the digits of the value
        for digit in str(value):
            # Check if the digit is a happy digit
            if int(digit) % k == 0:
                # Add the digit to the set of happy digits
                happy_digits.add(int(digit))
    
    # Return the set of happy digits
    return happy_digits


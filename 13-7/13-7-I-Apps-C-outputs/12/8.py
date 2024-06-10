
def get_divine_digits(n, k, a):
    # Initialize a set to store the divine digits
    divine_digits = set()
    
    # Iterate over the denominations of banknotes
    for i in range(n):
        # Get the value of the current banknote
        value = a[i]
        
        # Iterate over the digits of the current banknote
        for digit in str(value):
            # Check if the digit is a divine digit
            if digit in str(k):
                # Add the digit to the set of divine digits
                divine_digits.add(digit)
    
    # Return the set of divine digits
    return divine_digits

def get_happy_values(n, k, a, divine_digits):
    # Initialize a list to store the happy values
    happy_values = []
    
    # Iterate over the denominations of banknotes
    for i in range(n):
        # Get the value of the current banknote
        value = a[i]
        
        # Iterate over the digits of the current banknote
        for digit in str(value):
            # Check if the digit is a divine digit
            if digit in divine_digits:
                # Add the value to the list of happy values
                happy_values.append(value)
                break
    
    # Return the list of happy values
    return happy_values

def main():
    # Read the input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Get the divine digits
    divine_digits = get_divine_digits(n, k, a)
    
    # Get the happy values
    happy_values = get_happy_values(n, k, a, divine_digits)
    
    # Print the number of happy values
    print(len(happy_values))
    
    # Print the happy values in increasing order
    print(*sorted(happy_values))

if __name__ == '__main__':
    main()


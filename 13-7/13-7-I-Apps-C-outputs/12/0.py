
def get_divine_digits(n, k, a):
    # Initialize a set to store the divine digits
    divine_digits = set()
    
    # Iterate over the banknote denominations
    for i in range(n):
        # Get the value of the current banknote
        value = a[i]
        
        # Iterate over the digits of the value
        for digit in str(value):
            # If the digit is the divine digit, add it to the set
            if digit == str(k - 1):
                divine_digits.add(digit)
    
    # Return the set of divine digits
    return divine_digits

def get_happy_values(n, k, a, divine_digits):
    # Initialize a list to store the happy values
    happy_values = []
    
    # Iterate over the banknote denominations
    for i in range(n):
        # Get the value of the current banknote
        value = a[i]
        
        # Iterate over the digits of the value
        for digit in str(value):
            # If the digit is a divine digit, add the value to the list
            if digit in divine_digits:
                happy_values.append(value)
    
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
    
    # Print the happy values
    print(*happy_values)

if __name__ == '__main__':
    main()


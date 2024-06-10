
def get_divine_digits(n, k, a):
    # Initialize a set to store the divine digits
    divine_digits = set()
    
    # Iterate over the banknote denominations
    for i in range(n):
        # Get the value of the current banknote in the Martian number system
        value = int(str(a[i]), k)
        
        # Get the last digit of the value in the Martian number system
        last_digit = value % k
        
        # If the last digit is divine, add it to the set of divine digits
        if last_digit in [0, 4]:
            divine_digits.add(last_digit)
    
    # Return the set of divine digits
    return divine_digits

def get_possible_amounts(n, k, a, divine_digits):
    # Initialize a list to store the possible amounts
    possible_amounts = []
    
    # Iterate over the banknote denominations
    for i in range(n):
        # Get the value of the current banknote in the Martian number system
        value = int(str(a[i]), k)
        
        # Get the last digit of the value in the Martian number system
        last_digit = value % k
        
        # If the last digit is divine, add the current banknote value to the list of possible amounts
        if last_digit in divine_digits:
            possible_amounts.append(value)
    
    # Return the list of possible amounts
    return possible_amounts

def main():
    # Read the input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Get the set of divine digits
    divine_digits = get_divine_digits(n, k, a)
    
    # Get the list of possible amounts
    possible_amounts = get_possible_amounts(n, k, a, divine_digits)
    
    # Print the number of possible amounts
    print(len(possible_amounts))
    
    # Print the possible amounts in increasing order
    for amount in sorted(possible_amounts):
        print(amount)

if __name__ == '__main__':
    main()


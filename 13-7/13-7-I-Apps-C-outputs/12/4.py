
def get_divine_digits(n, k, a):
    # Initialize a set to store the divine digits
    divine_digits = set()
    
    # Iterate over the banknote denominations
    for i in range(n):
        # Get the value of the current banknote in the Martian number system
        value = convert_to_base_k(a[i], k)
        # Get the last digit of the value
        last_digit = value % k
        # If the last digit is divine, add it to the set of divine digits
        if last_digit in [0, 4]:
            divine_digits.add(last_digit)
    
    # Return the set of divine digits
    return divine_digits

def convert_to_base_k(n, k):
    # Initialize the result
    result = 0
    # Iterate while n is greater than 0
    while n > 0:
        # Get the last digit of n
        last_digit = n % k
        # Add the last digit to the result
        result = result * k + last_digit
        # Remove the last digit from n
        n //= k
    # Return the result
    return result

def main():
    # Read the input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # Get the divine digits
    divine_digits = get_divine_digits(n, k, a)
    # Print the number of divine digits
    print(len(divine_digits))
    # Print the divine digits
    print(*divine_digits)

if __name__ == '__main__':
    main()



def get_resistors(a, b):
    # Initialize the number of resistors to 0
    num_resistors = 0
    # While the resistance is not equal to the target resistance
    while a / b != 1:
        # If the resistance is even
        if a % 2 == 0 and b % 2 == 0:
            # Double the number of resistors and double the resistance
            num_resistors += 1
            a *= 2
            b *= 2
        # If the resistance is odd and the denominator is odd
        elif a % 2 == 1 and b % 2 == 1:
            # Increase the number of resistors and swap the numerator and denominator
            num_resistors += 1
            a, b = b, a
        # If the resistance is odd and the denominator is even
        elif a % 2 == 1 and b % 2 == 0:
            # Increase the number of resistors and add 1 to the numerator
            num_resistors += 1
            a += 1
    
    # Return the number of resistors
    return num_resistors

def main():
    # Read the input
    a, b = map(int, input().split())
    # Call the function to get the number of resistors
    num_resistors = get_resistors(a, b)
    # Print the output
    print(num_resistors)

if __name__ == '__main__':
    main()



def get_resistors(a, b):
    # Initialize the number of resistors needed
    num_resistors = 0
    
    # While the resistance is not equal to the target resistance
    while a / b != 1:
        # If the resistance is even
        if a % 2 == 0 and b % 2 == 0:
            # Double the resistance
            a *= 2
            b *= 2
        # If the resistance is odd
        else:
            # Increment the number of resistors needed
            num_resistors += 1
            # Reduce the resistance by 1
            a -= 1
    
    # Return the number of resistors needed
    return num_resistors

def main():
    # Read the input
    a, b = map(int, input().split())
    
    # Call the get_resistors function
    num_resistors = get_resistors(a, b)
    
    # Print the number of resistors needed
    print(num_resistors)

if __name__ == '__main__':
    main()


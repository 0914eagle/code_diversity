
def get_resistors_needed(a, b):
    # Initialize the number of resistors needed to 0
    resistors_needed = 0
    
    # While the resistance is not equal to the target resistance
    while a / b != 1:
        # If the resistance is less than 1
        if a / b < 1:
            # Increase the number of resistors needed
            resistors_needed += 1
            # Double the resistance
            a *= 2
        # If the resistance is greater than 1
        else:
            # Decrease the number of resistors needed
            resistors_needed -= 1
            # Half the resistance
            b *= 2
    
    # Return the number of resistors needed
    return resistors_needed

def main():
    # Read the input
    a, b = map(int, input().split())
    
    # Call the function to get the number of resistors needed
    resistors_needed = get_resistors_needed(a, b)
    
    # Print the output
    print(resistors_needed)

if __name__ == '__main__':
    main()


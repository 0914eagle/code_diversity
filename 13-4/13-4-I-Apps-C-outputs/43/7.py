
def get_resistors(a, b):
    # Initialize the number of resistors to 0
    num_resistors = 0
    # Initialize the current resistance to 0
    current_resistance = 0
    # Loop until the current resistance is equal to the target resistance
    while current_resistance != a/b:
        # If the current resistance is less than the target resistance, connect resistors in parallel
        if current_resistance < a/b:
            # Increment the number of resistors
            num_resistors += 1
            # Calculate the new resistance
            current_resistance = 1/(1/current_resistance + 1/b)
        # If the current resistance is greater than the target resistance, connect resistors in series
        else:
            # Decrement the number of resistors
            num_resistors -= 1
            # Calculate the new resistance
            current_resistance = current_resistance - b
    # Return the number of resistors
    return num_resistors

def main():
    # Read the input
    a, b = map(int, input().split())
    # Call the get_resistors function and print the result
    print(get_resistors(a, b))

if __name__ == '__main__':
    main()


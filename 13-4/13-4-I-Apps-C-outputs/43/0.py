
def get_resistors(a, b):
    # Initialize the number of resistors needed
    num_resistors = 0
    
    # While the resistance is not equal to the target resistance
    while a / b != 1:
        # If the resistance is not a whole number
        if a % b != 0:
            # Increment the number of resistors needed
            num_resistors += 1
            # Divide the resistance by the number of resistors
            a = a // b
        # If the resistance is a whole number
        else:
            # Break out of the loop
            break
    
    # Return the number of resistors needed
    return num_resistors

def main():
    # Read the input
    a, b = map(int, input().split())
    
    # Call the get_resistors function and print the result
    print(get_resistors(a, b))

if __name__ == '__main__':
    main()


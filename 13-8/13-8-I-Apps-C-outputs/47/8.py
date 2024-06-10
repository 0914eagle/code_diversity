
def get_min_steps(a, b):
    # Initialize the minimum number of steps as 0
    min_steps = 0
    
    # While the two numbers are not equal
    while a != b:
        # If the first number is greater than the second number
        if a > b:
            # Subtract 1 from the first number and add 1 to the second number
            a -= 1
            b += 1
        # If the second number is greater than the first number
        else:
            # Subtract 1 from the second number and add 1 to the first number
            b -= 1
            a += 1
        
        # Increment the minimum number of steps
        min_steps += 1
    
    # Return the minimum number of steps
    return min_steps

def main():
    # Read the input from stdin
    a, b = map(int, input().split())
    
    # Print the minimum number of steps required to add the two numbers
    print(get_min_steps(a, b))

if __name__ == '__main__':
    main()


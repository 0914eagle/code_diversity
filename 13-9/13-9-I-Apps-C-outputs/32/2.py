
def get_number_of_steps(num1, num2):
    # Initialize variables
    steps = 0
    carry = 0
    
    # Loop until the numbers can be added without any carry digits
    while num1 + num2 + carry > 0:
        # Add 1 to one of the numbers and subtract 1 from the other
        if num1 > num2:
            num1 -= 1
            num2 += 1
        else:
            num1 += 1
            num2 -= 1
        
        # Update the carry digit
        carry = 1 if num1 + num2 + carry > 0 else 0
        
        # Increment the number of steps
        steps += 1
    
    # Return the number of steps
    return steps

def main():
    # Read the input
    num1 = int(input())
    num2 = int(input())
    
    # Call the function to get the number of steps
    steps = get_number_of_steps(num1, num2)
    
    # Print the output
    print(steps)

if __name__ == '__main__':
    main()



def get_min_steps(num1, num2):
    # Convert the numbers to strings
    num1_str = str(num1)
    num2_str = str(num2)
    
    # Initialize the minimum number of steps
    min_steps = 0
    
    # Loop through the digits of both numbers
    for i in range(len(num1_str)):
        # Get the digits of both numbers at the current position
        num1_digit = int(num1_str[i])
        num2_digit = int(num2_str[i])
        
        # If the digits are not equal, perform the addition
        if num1_digit != num2_digit:
            # If the digit of num1 is greater, subtract 1 from num2
            if num1_digit > num2_digit:
                num2_str = num2_str[:i] + str(int(num2_str[i]) - 1) + num2_str[i+1:]
            # If the digit of num2 is greater, subtract 1 from num1
            else:
                num1_str = num1_str[:i] + str(int(num1_str[i]) - 1) + num1_str[i+1:]
                
            # Increment the minimum number of steps
            min_steps += 1
    
    # Return the minimum number of steps
    return min_steps

def main():
    # Read the input
    num1, num2 = map(int, input().split())
    
    # Get the minimum number of steps
    min_steps = get_min_steps(num1, num2)
    
    # Print the minimum number of steps
    print(min_steps)

if __name__ == '__main__':
    main()


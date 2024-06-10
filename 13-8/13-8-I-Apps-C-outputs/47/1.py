
def get_number_of_steps(num1, num2):
    # Initialize variables
    count = 0
    diff = num1 - num2
    
    # Check if the difference is negative
    if diff < 0:
        diff = -diff
    
    # Loop until the difference is 0 or 1
    while diff > 1:
        count += 1
        diff = diff // 10
    
    # Return the number of steps
    return count

def main():
    # Read the input
    num1 = int(input())
    num2 = int(input())
    
    # Call the function to get the number of steps
    count = get_number_of_steps(num1, num2)
    
    # Print the output
    print(count)

if __name__ == '__main__':
    main()


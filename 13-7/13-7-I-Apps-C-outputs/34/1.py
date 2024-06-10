
def get_carry_digit(num1, num2):
    # Calculate the sum of the two numbers
    sum = num1 + num2
    
    # Check if the sum is greater than 9
    if sum > 9:
        # If the sum is greater than 9, return 1 as the carry digit
        return 1
    else:
        # If the sum is less than or equal to 9, return 0 as the carry digit
        return 0

def get_steps(num1, num2):
    # Initialize a variable to keep track of the number of steps
    steps = 0
    
    # While the two numbers cannot be added without carry digits using the standard algorithm
    while get_carry_digit(num1, num2) == 1:
        # Add 1 to one of the numbers and subtract 1 from the other
        num1 += 1
        num2 -= 1
        
        # Increment the number of steps
        steps += 1
    
    # Return the number of steps
    return steps

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_steps(num1, num2))


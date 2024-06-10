
def get_carry_steps(num1, num2):
    # Initialize variables
    steps = 0
    carry = 0
    
    # Loop through the digits of both numbers
    while num1 > 0 and num2 > 0:
        # Calculate the sum of the digits at the same position in both numbers
        sum_digits = num1 % 10 + num2 % 10 + carry
        
        # Check if the sum exceeds 9
        if sum_digits > 9:
            # If it does, add a carry digit and subtract 10 from the smaller number
            carry = 1
            if num1 > num2:
                num1 -= 10
            else:
                num2 -= 10
        else:
            # If the sum is less than or equal to 9, no carry digit is needed
            carry = 0
        
        # Update the number of steps
        steps += 1
        
        # Update the numbers
        num1 //= 10
        num2 //= 10
    
    # Return the number of steps
    return steps

def get_carry_steps_alt(num1, num2):
    # Initialize variables
    steps = 0
    carry = 0
    
    # Loop through the digits of both numbers
    while num1 > 0 and num2 > 0:
        # Calculate the sum of the digits at the same position in both numbers
        sum_digits = num1 % 10 + num2 % 10 + carry
        
        # Check if the sum exceeds 9
        if sum_digits > 9:
            # If it does, add a carry digit and subtract 10 from the smaller number
            carry = 1
            if num1 > num2:
                num1 -= 10
            else:
                num2 -= 10
        else:
            # If the sum is less than or equal to 9, no carry digit is needed
            carry = 0
        
        # Update the number of steps
        steps += 1
        
        # Update the numbers
        num1 //= 10
        num2 //= 10
    
    # Return the number of steps
    return steps

if __name__ == '__main__':
    num1, num2 = map(int, input().split())
    print(get_carry_steps(num1, num2))
    print(get_carry_steps_alt(num1, num2))


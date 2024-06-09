
def solve(n, m, digits):
    # Initialize the smallest integer as -1
    smallest = -1
    
    # Iterate through all possible integers with n digits
    for i in range(10**(n-1), 10**n):
        # Convert the integer to a list of digits
        digit_list = list(str(i))
        
        # Check if the digit list has the required length
        if len(digit_list) != n:
            continue
        
        # Check if the digit list satisfies the conditions
        for j in range(m):
            if digit_list[digits[j]-1] != str(j+1):
                break
        else:
            # If all conditions are satisfied, update the smallest integer
            smallest = i
            break
    
    # Return the smallest integer
    return smallest


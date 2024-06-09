
def get_largest_sum(n):
    # Initialize variables
    max_sum = 0
    a = 0
    b = 0
    
    # Iterate through all possible values of a
    for i in range(n+1):
        # Calculate b as the difference between n and a
        b = n - i
        
        # Calculate the sum of digits in the base 10 representation of a and b
        sum_a = sum(int(digit) for digit in str(i))
        sum_b = sum(int(digit) for digit in str(b))
        
        # Calculate the total sum
        total_sum = sum_a + sum_b
        
        # If the total sum is larger than the current maximum, update the maximum and the values of a and b
        if total_sum > max_sum:
            max_sum = total_sum
            a = i
            b = b
    
    # Return the largest sum and the values of a and b
    return max_sum, a, b


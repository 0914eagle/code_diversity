
def largest_sum(n):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through all possible values of a
    for a in range(n+1):
        # Find the value of b that satisfies the condition a+b=n and a,b>=0
        b = n-a
        # If b is non-negative
        if b >= 0:
            # Calculate the sum of digits in the base 10 representation of a and b
            sum_a = sum(int(digit) for digit in str(a))
            sum_b = sum(int(digit) for digit in str(b))
            # If the sum of digits is larger than the current maximum, update the maximum sum
            if sum_a + sum_b > max_sum:
                max_sum = sum_a + sum_b
    # Return the maximum sum
    return max_sum


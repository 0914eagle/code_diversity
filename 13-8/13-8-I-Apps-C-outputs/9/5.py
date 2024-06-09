
def solve(n):
    # Initialize the maximum sum as 0
    max_sum = 0
    # Loop through all possible values of a
    for a in range(n+1):
        # Find the corresponding value of b
        b = n-a
        # Calculate the sum of digits in a and b
        sum_a = sum(int(digit) for digit in str(a))
        sum_b = sum(int(digit) for digit in str(b))
        # Update the maximum sum if necessary
        if sum_a + sum_b > max_sum:
            max_sum = sum_a + sum_b
    # Return the maximum sum
    return max_sum


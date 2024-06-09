
def solve(n):
    # Initialize the maximum sum as 0
    max_sum = 0
    # Loop through all possible values of a
    for a in range(n+1):
        # Find the corresponding value of b
        b = n - a
        # Calculate the sum of digits in a and b
        sum_a = sum_digits(a)
        sum_b = sum_digits(b)
        # Update the maximum sum if necessary
        max_sum = max(max_sum, sum_a + sum_b)
    # Return the maximum sum
    return max_sum

def sum_digits(n):
    # Initialize the sum as 0
    sum = 0
    # Loop through the digits of n
    while n > 0:
        # Add the last digit to the sum
        sum += n % 10
        # Remove the last digit
        n //= 10
    # Return the sum
    return sum


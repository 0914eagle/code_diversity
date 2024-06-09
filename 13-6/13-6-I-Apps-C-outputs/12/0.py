
def solve(n):
    # Initialize the maximum sum as 0
    max_sum = 0
    # Loop through all possible values of a
    for a in range(n+1):
        # Find the corresponding value of b
        b = n-a
        # Calculate the sum of digits in a and b
        sum_a = sum_digits(a)
        sum_b = sum_digits(b)
        # Check if a and b satisfy the conditions
        if a <= n and b <= n and a + b == n:
            # Calculate the total sum
            total_sum = sum_a + sum_b
            # Check if the total sum is greater than the maximum sum
            if total_sum > max_sum:
                # Update the maximum sum
                max_sum = total_sum
    # Return the maximum sum
    return max_sum

# Function to calculate the sum of digits in a number
def sum_digits(n):
    # Initialize the sum as 0
    sum = 0
    # Loop through the digits of the number
    while n > 0:
        # Add the last digit to the sum
        sum += n % 10
        # Remove the last digit from the number
        n //= 10
    # Return the sum
    return sum


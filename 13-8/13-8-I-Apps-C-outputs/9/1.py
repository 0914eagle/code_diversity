
def solve(n):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through all possible values of a
    for a in range(n+1):
        # Find the corresponding value of b
        b = n - a
        # Calculate the sum of digits in a and b
        sum_a = sum_digits(a)
        sum_b = sum_digits(b)
        # Check if the sum of digits is greater than the maximum sum
        if sum_a + sum_b > max_sum:
            # If yes, update the maximum sum and the values of a and b
            max_sum = sum_a + sum_b
            best_a = a
            best_b = b
    # Return the values of a and b with the maximum sum of digits
    return (best_a, best_b)

def sum_digits(n):
    # Initialize the sum to 0
    sum = 0
    # Loop through the digits of n
    while n > 0:
        # Add the last digit of n to the sum
        sum += n % 10
        # Remove the last digit of n
        n //= 10
    # Return the sum
    return sum


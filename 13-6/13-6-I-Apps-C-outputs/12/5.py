
def largest_sum_of_digit_sums(n):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through all possible values of a
    for a in range(n+1):
        # Calculate b from the given condition a + b = n
        b = n - a
        # Calculate the sum of digits in a and b
        sum_a = sum_digits(a)
        sum_b = sum_digits(b)
        # Calculate the current sum of digit sums
        current_sum = sum_a + sum_b
        # Update the maximum sum if necessary
        if current_sum > max_sum:
            max_sum = current_sum
    # Return the maximum sum
    return max_sum

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


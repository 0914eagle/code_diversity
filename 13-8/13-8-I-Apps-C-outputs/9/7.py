
def largest_sum_of_digit_pairs(n):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through all possible values of a
    for a in range(n + 1):
        # Find the corresponding value of b
        b = n - a
        # Calculate the sum of the digits in a and b
        sum_of_digits = sum_of_digits_in_base_10(a) + sum_of_digits_in_base_10(b)
        # Update the maximum sum if necessary
        if sum_of_digits > max_sum:
            max_sum = sum_of_digits
    # Return the maximum sum
    return max_sum

def sum_of_digits_in_base_10(n):
    # Initialize the sum to 0
    sum = 0
    # Loop while n is not 0
    while n > 0:
        # Add the last digit of n to the sum
        sum += n % 10
        # Divide n by 10 to get the next digit
        n //= 10
    # Return the sum
    return sum


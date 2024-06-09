
def largest_sum_of_digits(n):
    # Initialize the maximum sum of digits as 0
    max_sum = 0
    # Loop through all possible values of a
    for a in range(n+1):
        # Find the corresponding value of b
        b = n - a
        # Calculate the sum of digits of a and b
        sum_of_digits = sum_of_digits_in_base_10(a) + sum_of_digits_in_base_10(b)
        # Update the maximum sum of digits if necessary
        if sum_of_digits > max_sum:
            max_sum = sum_of_digits
    # Return the maximum sum of digits
    return max_sum

def sum_of_digits_in_base_10(n):
    # Initialize the sum of digits as 0
    sum_of_digits = 0
    # Loop through the digits of n
    while n > 0:
        # Add the current digit to the sum of digits
        sum_of_digits += n % 10
        # Divide n by 10 to move to the next digit
        n //= 10
    # Return the sum of digits
    return sum_of_digits


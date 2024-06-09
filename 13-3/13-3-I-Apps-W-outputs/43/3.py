
def smallest_sum_of_digits(k):
    # Initialize a variable to store the smallest sum
    smallest_sum = float('inf')
    # Loop through all positive multiples of k
    for i in range(1, 100001):
        # Calculate the sum of the digits in the decimal notation of the multiple
        sum_of_digits = sum([int(digit) for digit in str(i * k)])
        # Check if the sum is smaller than the current smallest sum
        if sum_of_digits < smallest_sum:
            # If so, update the smallest sum
            smallest_sum = sum_of_digits
    # Return the smallest sum
    return smallest_sum


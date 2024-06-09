
def get_min_diff(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the minimum difference and the final sum
    min_diff = 0
    final_sum = 0
    # Loop through the numbers and perform the operations
    for i in range(len(numbers)):
        # Round the current number to the nearest integer that isn't more than the current number
        rounded_num = int(numbers[i] + 0.5)
        # Update the final sum with the rounded number
        final_sum += rounded_num
        # Calculate the difference between the final sum and the sum of the original numbers
        diff = abs(final_sum - sum(numbers))
        # Update the minimum difference if the current difference is smaller than the previous minimum difference
        if i > 0 and diff < min_diff:
            min_diff = diff
    # Return the minimum difference
    return min_diff



def get_min_diff(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the minimum difference and the final sum
    min_diff = 0
    final_sum = 0
    # Loop through the numbers and perform the operations
    for i in range(len(numbers)):
        # Round the current number to the nearest integer that isn't more than the current number
        rounded_number = int(numbers[i] + 0.5)
        # Update the final sum with the rounded number
        final_sum += rounded_number
        # Calculate the difference between the final sum and the current sum
        diff = final_sum - sum(numbers[:i+1])
        # Update the minimum difference if necessary
        if i > 0 and diff < min_diff:
            min_diff = diff
    # Return the minimum difference
    return min_diff


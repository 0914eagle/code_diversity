
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
        # Calculate the difference between the rounded number and the current number
        diff = rounded_num - numbers[i]
        # Update the minimum difference if necessary
        if i > 0 and diff != 0:
            min_diff = min(min_diff, diff)
        # Update the final sum
        final_sum += rounded_num
    # Return the minimum difference
    return min_diff


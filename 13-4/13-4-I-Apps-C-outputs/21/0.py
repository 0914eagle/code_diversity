
def get_min_diff(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the minimum difference and the current sum
    min_diff = 0
    current_sum = 0
    # Iterate through the numbers
    for i in range(len(numbers)):
        # Calculate the current sum
        current_sum += numbers[i]
        # If it is not the last number, calculate the difference between the current sum and the sum of the remaining numbers
        if i != len(numbers) - 1:
            diff = abs(current_sum - sum(numbers[i+1:]))
            # Update the minimum difference if necessary
            if diff < min_diff or min_diff == 0:
                min_diff = diff
    # Return the minimum difference
    return min_diff


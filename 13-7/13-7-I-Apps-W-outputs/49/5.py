
def largest_sum_of_squares(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the result
    result = 0
    # Loop through the numbers
    for i in range(len(numbers)):
        # Calculate the sum of squares up to the current number
        result += numbers[i] ** 2
        # If there are more numbers after the current one, calculate the sum of squares between the current and next numbers
        if i + 1 < len(numbers):
            result += (numbers[i + 1] - numbers[i]) ** 2
    return result


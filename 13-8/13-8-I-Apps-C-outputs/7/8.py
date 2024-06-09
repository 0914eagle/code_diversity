
def get_maximum_xor_sum(numbers):
    # Sort the numbers in descending order
    numbers.sort(reverse=True)
    # Initialize the maximum xor sum and the corresponding subset
    max_xor_sum = 0
    subset = []
    # Iterate over the numbers
    for i, num in enumerate(numbers):
        # If the xor sum of the current subset and the current number is greater than the maximum xor sum, update the maximum xor sum and the corresponding subset
        xor_sum = sum(subset) ^ num
        if xor_sum > max_xor_sum:
            max_xor_sum = xor_sum
            subset = [num]
        # If the xor sum of the current subset and the current number is equal to the maximum xor sum, add the current number to the subset
        elif xor_sum == max_xor_sum:
            subset.append(num)
    # Return the maximum xor sum
    return max_xor_sum


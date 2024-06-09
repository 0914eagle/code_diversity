
def get_maximal_xor_sum(numbers):
    # Sort the numbers in descending order
    numbers.sort(reverse=True)
    # Initialize the maximum xor sum and its corresponding subset
    max_xor_sum = 0
    subset = []
    # Iterate over the numbers
    for i, num in enumerate(numbers):
        # If the current number is greater than the maximum xor sum, update the maximum xor sum and its corresponding subset
        if num > max_xor_sum:
            max_xor_sum = num
            subset = [num]
        # If the current number is equal to the maximum xor sum, add it to the subset
        elif num == max_xor_sum:
            subset.append(num)
    # Return the maximum xor sum
    return max_xor_sum


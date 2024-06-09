
def get_max_sum(n, a, b):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Iterate over all possible subsets of students
    for i in range(1 << n):
        # Initialize the current sum to 0
        current_sum = 0
        # Iterate over all students in the current subset
        for j in range(n):
            # Check if the j-th student is in the current subset
            if i & (1 << j):
                # Add the skill level of the j-th student to the current sum
                current_sum += b[j]
        # Check if the current sum is greater than the maximum sum
        if current_sum > max_sum:
            # Update the maximum sum
            max_sum = current_sum
    # Return the maximum sum
    return max_sum


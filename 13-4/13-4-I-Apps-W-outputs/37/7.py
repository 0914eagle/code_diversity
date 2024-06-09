
def get_min_operations(x):
    # Initialize the minimum number of operations to infinity
    min_operations = float('inf')
    # Iterate over all possible values of the die
    for i in range(1, 7):
        # Calculate the sum of the two numbers on opposite sides
        sum_of_opposite_sides = i + (6 - i)
        # Check if the sum is greater than or equal to x
        if sum_of_opposite_sides >= x:
            # If the sum is greater than or equal to x, return the minimum number of operations needed to reach this sum
            return min_operations
        # Otherwise, calculate the minimum number of operations needed to reach the sum
        min_operations = min(min_operations, abs(sum_of_opposite_sides - x))
    # Return the minimum number of operations needed to reach the sum
    return min_operations


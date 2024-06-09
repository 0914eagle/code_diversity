
def solve(x):
    # Initialize the minimum number of operations to infinity
    min_operations = float('inf')
    # Iterate over all possible values of the side facing upward
    for i in range(1, 7):
        # Calculate the sum of the two numbers on opposite sides
        sum_opposite_sides = i + (7 - i)
        # If the sum is greater than or equal to x, we can stop
        if sum_opposite_sides >= x:
            # Return the minimum number of operations needed to reach this sum
            return min_operations
        # Otherwise, calculate the minimum number of operations needed to reach this sum
        min_operations = min(min_operations, abs(sum_opposite_sides - x))
    # If we reach this point, it means that we could not reach x with any of the sides facing upward
    # So, we return the minimum number of operations needed to reach the closest sum to x
    return min_operations


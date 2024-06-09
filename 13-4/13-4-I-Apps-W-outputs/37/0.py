
def solve(x):
    # Initialize the minimum number of operations to infinity
    min_operations = float('inf')
    # Iterate over all possible values of the die
    for i in range(1, 7):
        # Initialize the current sum to the value of the current die
        current_sum = i
        # Initialize the number of operations to 0
        operations = 0
        # While the current sum is less than the target sum
        while current_sum < x:
            # Rotate the die toward the right
            current_sum += i
            operations += 1
        # If the current sum is greater than or equal to the target sum and the number of operations is less than the minimum number of operations
        if current_sum >= x and operations < min_operations:
            # Update the minimum number of operations
            min_operations = operations
    # Return the minimum number of operations
    return min_operations


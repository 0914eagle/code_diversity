
def solve(x):
    # Initialize the minimum number of operations to be infinite
    min_operations = float('inf')
    # Iterate over all possible values of the side facing upward
    for i in range(1, 7):
        # Initialize the current score to be 0
        current_score = 0
        # Initialize the current operation to be 0
        current_operation = 0
        # Iterate until the current score is greater than or equal to x
        while current_score < x:
            # Add the value of the current side to the current score
            current_score += i
            # Increment the current operation by 1
            current_operation += 1
            # If the current operation is odd, rotate the die 90 degrees to the left
            if current_operation % 2 == 1:
                i = (i - 1) % 6 + 1
            # If the current operation is even, rotate the die 90 degrees to the right
            else:
                i = (i + 1) % 6 + 1
        # If the current score is greater than or equal to x and the current operation is less than the minimum number of operations, update the minimum number of operations
        if current_score >= x and current_operation < min_operations:
            min_operations = current_operation
    # Return the minimum number of operations
    return min_operations



def solve(x):
    # Initialize the minimum number of operations to be performed
    min_operations = 0
    # Initialize the current score to be 0
    current_score = 0
    # Initialize the side of the die that is facing upward to be 1
    upward_side = 1

    # Loop until the current score is greater than or equal to x
    while current_score < x:
        # Increment the minimum number of operations to be performed
        min_operations += 1
        # Increment the current score by the number on the upward side of the die
        current_score += upward_side
        # Rotate the die 90 degrees clockwise
        upward_side = (upward_side + 1) % 6

    # Return the minimum number of operations needed to score at least x points
    return min_operations


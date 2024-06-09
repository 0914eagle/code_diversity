
def solve(x):
    # Initialize the minimum number of operations to perform
    min_operations = 0
    # Initialize the current score to 0
    current_score = 0
    # Initialize the die sides as a list of tuples (value, facing up)
    die_sides = [(1, True), (2, False), (3, False), (4, False), (5, False), (6, False)]

    # Loop until the current score is greater than or equal to x
    while current_score < x:
        # Find the side that is facing up
        facing_up_side = next(side for side in die_sides if side[1] is True)
        # Get the value of the facing up side
        facing_up_value = facing_up_side[0]
        # Add the value to the current score
        current_score += facing_up_value
        # Update the die sides by rotating it 90 degrees clockwise
        die_sides = [(die_sides[i][0], not die_sides[i][1]) for i in range(len(die_sides))]
        # Increment the minimum number of operations
        min_operations += 1

    # Return the minimum number of operations required to score at least x points
    return min_operations


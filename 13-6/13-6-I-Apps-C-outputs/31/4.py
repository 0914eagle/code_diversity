
def solve(balls):
    # Initialize the minimum number of operations to 0
    min_operations = 0

    # Loop through the balls
    for i in range(len(balls)):
        # Check if the current ball is white
        if balls[i][0] == "W":
            # Check if the next ball is also white
            if i < len(balls) - 1 and balls[i+1][0] == "W":
                # Swap the two white balls
                balls[i], balls[i+1] = balls[i+1], balls[i]
                # Increment the minimum number of operations
                min_operations += 1

    # Return the minimum number of operations
    return min_operations


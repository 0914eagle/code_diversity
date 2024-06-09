
def solve(balls):
    # Initialize the minimum number of operations to 0
    min_operations = 0

    # Sort the balls by their values in ascending order
    sorted_balls = sorted(balls, key=lambda x: x[1])

    # Iterate through the sorted balls
    for i in range(len(sorted_balls)):
        # Check if the current ball is white and the next ball is also white
        if sorted_balls[i][0] == "W" and i + 1 < len(sorted_balls) and sorted_balls[i + 1][0] == "W":
            # Swap the current white ball with the next white ball
            sorted_balls[i], sorted_balls[i + 1] = sorted_balls[i + 1], sorted_balls[i]
            # Increment the minimum number of operations
            min_operations += 1

    # Return the minimum number of operations required to achieve the objective
    return min_operations


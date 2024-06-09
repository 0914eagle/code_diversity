
def solve(N, colors):
    # Initialize the number of operations to 0
    operations = 0

    # Loop through the colors of the stones
    for i in range(N):
        # If the current color is white and the next color is red, we need to perform an operation
        if colors[i] == "W" and colors[i+1] == "R":
            # Increment the number of operations
            operations += 1
            # Swap the current and next colors
            colors[i], colors[i+1] = colors[i+1], colors[i]

    # Return the number of operations needed
    return operations


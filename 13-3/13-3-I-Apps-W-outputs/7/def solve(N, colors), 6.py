
def solve(N, colors):
    # Initialize the number of operations to 0
    operations = 0

    # Loop through the colors from left to right
    for i in range(N):
        # If the current color is white and the next color is red, we need to swap them
        if colors[i] == "W" and colors[i+1] == "R":
            operations += 1
            # Swap the colors
            colors[i] = "R"
            colors[i+1] = "W"

    # Return the number of operations needed
    return operations


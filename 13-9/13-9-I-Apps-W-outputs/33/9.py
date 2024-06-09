
def solve(n, k):
    # Initialize the height of the plot as 0
    height = 0
    # Loop through each point in the plot
    for i in range(2*n+1):
        # If the point has an odd x-coordinate, increase the height by 1
        if i % 2 == 1:
            height += 1
        # If the point has an even x-coordinate, decrease the height by 1
        else:
            height -= 1
    # Return the minimum height that can have the plot with the given area
    return height



def solve(n, k):
    # Initialize the height of the plot as 0
    height = 0
    # Loop through each point in the plot
    for i in range(2*n+1):
        # If the point has an odd x-coordinate, increase its y-coordinate by 1
        if i % 2 == 1:
            height += 1
        # If the point has an even x-coordinate, check if the height is greater than the current y-coordinate
        else:
            height = max(height, i)
    # Return the height of the plot
    return height


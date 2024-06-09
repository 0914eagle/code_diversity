
def get_min_height(n, k):
    # Initialize the height as 0
    height = 0

    # Loop through each point and increase the height by 1 if the x-coordinate is odd
    for i in range(1, 2*n+1, 2):
        height += 1

    # Return the minimum height
    return height



def get_min_height(n, k):
    # Initialize the height as 0
    height = 0
    # Iterate through the points
    for i in range(n):
        # If the point has an odd x-coordinate, increase the height by 1
        if i % 2 == 1:
            height += 1
        # If the point has an even x-coordinate, increase the height by 2
        else:
            height += 2
    # Return the minimum height that can be reached
    return height


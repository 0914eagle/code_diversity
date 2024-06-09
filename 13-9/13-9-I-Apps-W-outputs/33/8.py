
def get_min_height(n, k):
    # Initialize the height of the plot as 0
    height = 0
    # Iterate through each point and increase the height if the x-coordinate is odd
    for i in range(1, 2*n+1, 2):
        height += 1
        k -= i
    # If the area is not 0, return -1 as there is no possible plot with the given area
    if k != 0:
        return -1
    # Return the height of the plot
    return height


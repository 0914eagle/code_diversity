
def get_min_watering_operations(heights):
    # Initialize variables
    n = len(heights)
    min_operations = 0
    max_height = max(heights)

    # Loop through each height and check if it is equal to the maximum height
    for i in range(n):
        if heights[i] < max_height:
            # If the height is not equal to the maximum height, increment the minimum number of operations
            min_operations += 1

    # Return the minimum number of operations required
    return min_operations


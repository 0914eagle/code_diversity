
def get_min_watering_operations(heights):
    # Initialize variables
    n = len(heights)
    min_operations = 0
    max_height = max(heights)

    # Loop through each height and check if it is greater than the current maximum height
    for i in range(n):
        if heights[i] > max_height:
            # If the height is greater than the current maximum height, increment the minimum number of operations
            min_operations += 1
            # Update the maximum height to the current height
            max_height = heights[i]

    return min_operations


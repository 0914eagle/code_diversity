
def get_min_watering_operations(heights):
    # Initialize variables
    n = len(heights)
    min_operations = 0
    max_height = max(heights)

    # Loop through each height and check if it can be reached
    for i in range(n):
        if heights[i] < max_height:
            # Increase the height of the current flower by 1
            heights[i] += 1
            min_operations += 1

    # Return the minimum number of watering operations required
    return min_operations


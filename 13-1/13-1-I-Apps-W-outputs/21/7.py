
def get_min_operations(heights):
    # Initialize variables
    operations = 0
    current_height = 0

    # Iterate through the heights and check if they are non-decreasing
    for i in range(len(heights)):
        if heights[i] <= current_height:
            current_height = heights[i]
        else:
            operations += 1
            current_height = heights[i]

    return operations



def get_max_triangles(sticks):
    # Sort the sticks in non-decreasing order
    sticks.sort()
    # Initialize the maximum number of triangles to 0
    max_triangles = 0
    # Iterate over the sticks
    for i in range(len(sticks)):
        # Get the length of the current stick
        length = sticks[i]
        # Find the number of sticks that are smaller than the current stick
        smaller_sticks = sum(1 for j in sticks if j < length)
        # Find the number of sticks that are larger than the current stick
        larger_sticks = sum(1 for j in sticks if j > length)
        # Update the maximum number of triangles
        max_triangles = max(max_triangles, smaller_sticks * larger_sticks)
    return max_triangles


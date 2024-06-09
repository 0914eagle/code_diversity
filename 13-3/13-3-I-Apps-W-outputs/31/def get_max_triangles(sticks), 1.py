
def get_max_triangles(sticks):
    # Sort the sticks in descending order
    sticks.sort(reverse=True)
    # Initialize the number of triangles to 0
    triangles = 0
    # Iterate over the sticks
    for i in range(len(sticks)):
        # Check if the current stick is divisible by 2
        if sticks[i] % 2 == 0:
            # Increment the number of triangles
            triangles += 1
            # Divide the current stick by 2
            sticks[i] //= 2
    # Return the number of triangles
    return triangles


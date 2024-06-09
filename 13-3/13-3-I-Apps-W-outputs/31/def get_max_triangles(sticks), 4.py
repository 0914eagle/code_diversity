
def get_max_triangles(sticks):
    # Sort the sticks in descending order
    sticks.sort(reverse=True)
    # Initialize the number of triangles to 0
    triangles = 0
    # Loop through the sticks
    for i in range(len(sticks)):
        # Check if the current stick is divisible by 3
        if sticks[i] % 3 == 0:
            # If it is, add the number of triangles that can be formed with this stick to the total
            triangles += sticks[i] // 3
        # Check if the current stick is divisible by 2
        if sticks[i] % 2 == 0:
            # If it is, add the number of triangles that can be formed with this stick to the total
            triangles += sticks[i] // 2
    # Return the total number of triangles
    return triangles


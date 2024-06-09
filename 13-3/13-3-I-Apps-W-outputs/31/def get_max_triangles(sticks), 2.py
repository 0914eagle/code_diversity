
def get_max_triangles(sticks):
    # Sort the sticks in descending order
    sticks.sort(reverse=True)
    # Initialize the number of triangles to 0
    triangles = 0
    # Loop through the sticks
    for i in range(len(sticks)):
        # Check if the current stick is divisible by 3
        if sticks[i] % 3 == 0:
            # Increment the number of triangles
            triangles += sticks[i] // 3
            # Subtract the current stick from the list
            sticks[i] = 0
        # Check if the current stick is divisible by 2
        elif sticks[i] % 2 == 0:
            # Increment the number of triangles
            triangles += sticks[i] // 2
            # Subtract the current stick from the list
            sticks[i] = 0
    # Return the number of triangles
    return triangles



def get_max_triangles(sticks):
    # Sort the sticks in descending order
    sticks.sort(reverse=True)
    # Initialize the number of triangles to 0
    triangles = 0
    # Iterate through the sticks
    for i in range(len(sticks)):
        # Check if the current stick is divisible by 3
        if sticks[i] % 3 == 0:
            # Increment the number of triangles
            triangles += sticks[i] // 3
            # Subtract the current stick from the list
            sticks[i] -= sticks[i] // 3 * 3
    return triangles


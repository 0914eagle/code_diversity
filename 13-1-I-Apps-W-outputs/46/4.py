
def solve(n):
    # Initialize the number of yellow vertices to 0
    yellow_vertices = 0
    
    # Loop through each level of the Rooted Dead Bush
    for level in range(1, n+1):
        # Calculate the number of vertices at the current level
        num_vertices = (level * (level + 1)) // 2
        
        # If the number of vertices is odd, we can choose a claw
        if num_vertices % 2 == 1:
            # Increment the number of yellow vertices
            yellow_vertices += 1
    
    # Return the number of yellow vertices modulo 10^9 + 7
    return yellow_vertices % 1000000007



def get_min_rod_length(triangle_list):
    
    # Initialize the minimum rod length to 0
    min_rod_length = 0

    # Iterate over the triangles in the list
    for triangle in triangle_list:
        # Calculate the length of the hypotenuse of the triangle
        hypotenuse = (triangle[0] ** 2 + triangle[1] ** 2) ** 0.5

        # Update the minimum rod length if necessary
        if hypotenuse > min_rod_length:
            min_rod_length = hypotenuse

    # Return the minimum rod length
    return min_rod_length


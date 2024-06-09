
def get_min_rod_length(triangles):
    
    # Initialize the minimum length to zero
    min_length = 0

    # Iterate over the triangles
    for triangle in triangles:
        # Calculate the length of the hypotenuse
        hypotenuse = (triangle[0] ** 2 + triangle[1] ** 2) ** 0.5

        # Update the minimum length if necessary
        if hypotenuse > min_length:
            min_length = hypotenuse

    # Return the minimum length
    return min_length


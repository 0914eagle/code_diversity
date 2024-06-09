
def get_min_rod_length(triangles):
    
    # Initialize the minimum length to zero
    min_length = 0

    # Iterate over the triangles
    for triangle in triangles:
        # Calculate the perimeter of the triangle
        perimeter = triangle[0] + triangle[1] + triangle[2]

        # Calculate the minimum length required for the rod
        min_length = max(min_length, perimeter / 2)

    # Return the minimum length
    return min_length


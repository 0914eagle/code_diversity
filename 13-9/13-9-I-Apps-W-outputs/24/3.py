
def find_last_visited_cafe(visited_cafes):
    # Sort the visited cafes in ascending order
    visited_cafes.sort()
    # Initialize the last visited cafe as the first cafe in the list
    last_visited_cafe = visited_cafes[0]
    # Iterate over the visited cafes starting from the second cafe
    for cafe in visited_cafes[1:]:
        # If the current cafe is different from the last visited cafe, update the last visited cafe
        if cafe != last_visited_cafe:
            last_visited_cafe = cafe
    # Return the last visited cafe
    return last_visited_cafe


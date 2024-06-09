
def find_last_visited_cafe(visited_cafes):
    # Sort the visited cafes in ascending order
    visited_cafes.sort()
    # Initialize a variable to keep track of the last visited cafe
    last_visited_cafe = visited_cafes[0]
    # Iterate through the list of visited cafes
    for cafe in visited_cafes:
        # If the current cafe is later than the last visited cafe, update the last visited cafe
        if cafe > last_visited_cafe:
            last_visited_cafe = cafe
    # Return the last visited cafe
    return last_visited_cafe


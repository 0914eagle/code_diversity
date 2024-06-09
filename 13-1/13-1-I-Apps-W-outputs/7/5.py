
def solve(w, h, n, cuts):
    # Initialize the maximum area and the current fragment
    max_area = 0
    current_fragment = [w, h]

    # Loop through each cut
    for cut in cuts:
        # Get the type of cut and the distance from the edge
        type, distance = cut.split(" ")
        distance = int(distance)

        # Update the current fragment based on the type of cut
        if type == "H":
            current_fragment[1] -= distance
        else:
            current_fragment[0] -= distance

        # Calculate the area of the current fragment
        area = current_fragment[0] * current_fragment[1]

        # Update the maximum area if necessary
        if area > max_area:
            max_area = area

    # Return the maximum area
    return max_area


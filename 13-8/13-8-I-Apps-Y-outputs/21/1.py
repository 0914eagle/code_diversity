
def get_escape_hole(gopher_coords, dog_coords, hole_coords):
    # Calculate the distance between the gopher and the dog
    distance = ((dog_coords[0] - gopher_coords[0]) ** 2 + (dog_coords[1] - gopher_coords[1]) ** 2) ** 0.5

    # Calculate the distance between the gopher and each hole
    hole_distances = []
    for hole in hole_coords:
        hole_distances.append(((hole[0] - gopher_coords[0]) ** 2 + (hole[1] - gopher_coords[1]) ** 2) ** 0.5)

    # Check if the gopher can escape through any hole
    for i in range(len(hole_coords)):
        if hole_distances[i] > distance:
            return f"The gopher can escape through the hole at ({hole_coords[i][0]}, {hole_coords[i][1]})."

    return "The gopher cannot escape."


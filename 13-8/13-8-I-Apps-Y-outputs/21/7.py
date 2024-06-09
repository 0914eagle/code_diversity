
def gopher_escape(gopher_coords, dog_coords, gopher_holes):
    # Calculate the distance between the gopher and the dog
    distance = ((dog_coords[0] - gopher_coords[0]) ** 2 + (dog_coords[1] - gopher_coords[1]) ** 2) ** 0.5

    # Calculate the distance between the gopher and each gopher hole
    hole_distances = []
    for hole in gopher_holes:
        hole_distances.append(((hole[0] - gopher_coords[0]) ** 2 + (hole[1] - gopher_coords[1]) ** 2) ** 0.5)

    # Check if the gopher can escape through any of the gopher holes
    for i in range(len(gopher_holes)):
        if hole_distances[i] > distance:
            return f"The gopher can escape through the hole at ({gopher_holes[i][0]}, {gopher_holes[i][1]})."

    return "The gopher cannot escape."



def gopher_hole(gopher, dog, holes):
    # Calculate the distance between the gopher and the dog
    distance = ((dog[0] - gopher[0]) ** 2 + (dog[1] - gopher[1]) ** 2) ** 0.5

    # Calculate the distance between the gopher and each hole
    hole_distances = []
    for hole in holes:
        hole_distance = ((hole[0] - gopher[0]) ** 2 + (hole[1] - gopher[1]) ** 2) ** 0.5
        hole_distances.append(hole_distance)

    # Check if the gopher can escape through any hole
    for i in range(len(holes)):
        if hole_distances[i] > distance:
            return f"The gopher can escape through the hole at ({holes[i][0]}, {holes[i][1]})."

    return "The gopher cannot escape."


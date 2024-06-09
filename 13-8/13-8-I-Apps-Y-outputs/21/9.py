
def solve(gopher, dog, holes):
    # Calculate the distance between the gopher and the dog
    distance = ((gopher[0] - dog[0]) ** 2 + (gopher[1] - dog[1]) ** 2) ** 0.5

    # Calculate the distance between the gopher and each hole
    hole_distances = []
    for hole in holes:
        hole_distance = ((gopher[0] - hole[0]) ** 2 + (gopher[1] - hole[1]) ** 2) ** 0.5
        hole_distances.append(hole_distance)

    # Check if the gopher can escape through any hole
    for i in range(len(holes)):
        if hole_distances[i] > distance:
            return f"The gopher can escape through the hole at ({holes[i][0]}, {holes[i][1]})."

    return "The gopher cannot escape."


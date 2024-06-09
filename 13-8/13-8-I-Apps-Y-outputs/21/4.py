
def find_escape_hole(gopher_coords, dog_coords, holes):
    gopher_x, gopher_y = gopher_coords
    dog_x, dog_y = dog_coords
    for hole_x, hole_y in holes:
        if hole_x == gopher_x and hole_y == gopher_y:
            return "The gopher can escape through the hole at ({}, {}).".format(hole_x, hole_y)
    return "The gopher cannot escape."


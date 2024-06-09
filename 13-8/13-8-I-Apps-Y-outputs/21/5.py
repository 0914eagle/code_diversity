
def solve(gopher_coords, dog_coords, gopher_holes):
    gopher_x, gopher_y = gopher_coords
    dog_x, dog_y = dog_coords
    for hole_x, hole_y in gopher_holes:
        if (hole_x - gopher_x) ** 2 + (hole_y - gopher_y) ** 2 < (dog_x - gopher_x) ** 2 + (dog_y - gopher_y) ** 2:
            return f"The gopher can escape through the hole at ({hole_x}, {hole_y})."
    return "The gopher cannot escape."


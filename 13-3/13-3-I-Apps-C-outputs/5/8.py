
def get_min_square_side(x_coords, y_coords, a, b):
    # Find the minimum x and y coordinates of the houses in the range [a, b]
    min_x = min(x_coords[a-1:b])
    min_y = min(y_coords[a-1:b])

    # Find the maximum x and y coordinates of the houses in the range [a, b]
    max_x = max(x_coords[a-1:b])
    max_y = max(y_coords[a-1:b])

    # Calculate the side length of the smallest square that contains all the houses
    side_length = max(max_x - min_x, max_y - min_y) + 1

    return side_length


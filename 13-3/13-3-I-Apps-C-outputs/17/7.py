
def get_shared_area(pine_trees, aspen_trees):
    pine_coords = [(x, y) for x, y in pine_trees]
    aspen_coords = [(x, y) for x, y in aspen_trees]
    total_area = 0
    for pine_coord in pine_coords:
        for aspen_coord in aspen_coords:
            area = get_triangle_area(pine_coord, aspen_coord)
            total_area += area
    return total_area

def get_triangle_area(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    area = 0.5 * abs(x1 * y2 - x2 * y1)
    return area


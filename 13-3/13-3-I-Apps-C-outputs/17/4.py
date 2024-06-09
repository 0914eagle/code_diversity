
def get_shared_area(pine_trees, aspen_trees):
    total_area = 0
    for pine in pine_trees:
        for aspen in aspen_trees:
            triangle_area = get_triangle_area(pine, aspen)
            total_area += triangle_area
    return total_area

def get_triangle_area(point1, point2):
    area = 0.5 * abs(point1[0] * point2[1] - point1[1] * point2[0])
    return area


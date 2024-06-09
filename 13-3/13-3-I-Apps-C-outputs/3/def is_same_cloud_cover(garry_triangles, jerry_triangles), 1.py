
def is_same_cloud_cover(garry_triangles, jerry_triangles):
    # Convert the triangles to a set of points
    garry_points = set()
    for triangle in garry_triangles:
        garry_points.update(triangle)

    jerry_points = set()
    for triangle in jerry_triangles:
        jerry_points.update(triangle)

    # Check if the two sets of points are equal
    return garry_points == jerry_points


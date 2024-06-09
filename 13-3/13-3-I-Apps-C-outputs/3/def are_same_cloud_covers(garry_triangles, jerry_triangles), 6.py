
def are_same_cloud_covers(garry_triangles, jerry_triangles):
    # Convert the triangles to a set of points
    garry_points = set()
    for triangle in garry_triangles:
        garry_points.update(triangle)

    jerry_points = set()
    for triangle in jerry_triangles:
        jerry_points.update(triangle)

    # Check if the sets of points are the same
    return garry_points == jerry_points


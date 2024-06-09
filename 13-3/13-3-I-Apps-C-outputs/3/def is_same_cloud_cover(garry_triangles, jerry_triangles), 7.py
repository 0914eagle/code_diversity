
def is_same_cloud_cover(garry_triangles, jerry_triangles):
    # Convert the triangles to a set of vertices
    garry_vertices = set()
    for triangle in garry_triangles:
        garry_vertices.update(triangle)

    jerry_vertices = set()
    for triangle in jerry_triangles:
        jerry_vertices.update(triangle)

    # Check if the sets of vertices are the same
    return garry_vertices == jerry_vertices


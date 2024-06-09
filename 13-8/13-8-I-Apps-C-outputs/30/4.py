
def canyon_mapping(n, k, vertices):
    
    # Sort the vertices in counterclockwise order
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Initialize the minimum side length of each map to the maximum possible value
    min_side_length = float('inf')

    # Iterate through all possible combinations of maps
    for map_indices in combinations(range(n), k):
        # Calculate the area of the current combination of maps
        area = 0
        for i in range(k):
            # Calculate the area of each map
            map_area = 0
            for j in range(n):
                if j in map_indices[i]:
                    map_area += (sorted_vertices[j][0] * sorted_vertices[(j+1)%n][1]) - (sorted_vertices[j][1] * sorted_vertices[(j+1)%n][0])
            area += abs(map_area) / 2

        # If the current combination of maps covers the entire polygon, update the minimum side length
        if area == 0:
            min_side_length = min(min_side_length, sorted_vertices[map_indices[0]][0] - sorted_vertices[map_indices[k-1]][0])

    return min_side_length


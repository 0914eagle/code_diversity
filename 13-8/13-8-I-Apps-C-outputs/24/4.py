
def get_minimum_spanning_tree_weight(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a disjoint set data structure to keep track of the connected components
    dsu = DisjointSetUnion(points)

    # Initialize the total weight of the minimum spanning tree to 0
    total_weight = 0

    # Iterate through all pairs of points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            # Calculate the weight of the edge between the two points
            weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

            # If the weight is less than or equal to the weight of the edge between the two points' connected components, merge the two components
            if weight <= dsu.find_set(points[i])[1]:
                dsu.union_sets(points[i], points[j])

            # Add the weight of the edge to the total weight of the minimum spanning tree
            total_weight += weight

    # Return the total weight of the minimum spanning tree
    return total_weight



def find_minimum_spanning_tree(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a dictionary to store the edges of the minimum spanning tree
    mst = {}

    # Loop through the points and add the edges to the minimum spanning tree
    for i in range(len(sorted_points)):
        current_point = sorted_points[i]
        for j in range(i+1, len(sorted_points)):
            next_point = sorted_points[j]
            distance = abs(current_point[0] - next_point[0]) + abs(current_point[1] - next_point[1])
            mst[(current_point, next_point)] = distance

    # Find the minimum weight edge in the minimum spanning tree
    min_weight = float('inf')
    for edge, weight in mst.items():
        if weight < min_weight:
            min_weight = weight

    return min_weight



def solve(n, vertices):
    # Sort the vertices by their x-coordinate
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Initialize the maximum circumference for each vertex
    max_circumference = [0] * n

    # Loop through each vertex and find the maximum circumference
    for i in range(n):
        # Find the two vertices with the minimum distance to the current vertex
        min_distance = float("inf")
        min_distance_vertices = []
        for j in range(n):
            if i != j:
                distance = distance_between_points(sorted_vertices[i], sorted_vertices[j])
                if distance < min_distance:
                    min_distance = distance
                    min_distance_vertices = [j]
                elif distance == min_distance:
                    min_distance_vertices.append(j)

        # Find the maximum circumference for the current vertex
        max_circumference[i] = 0
        for j in min_distance_vertices:
            max_circumference[i] = max(max_circumference[i], max_circumference[j] + min_distance)

    return max_circumference

def distance_between_points(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


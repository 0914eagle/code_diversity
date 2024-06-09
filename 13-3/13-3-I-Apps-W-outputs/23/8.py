
def find_closest_angle(n, a):
    # Initialize a list to store the vertices
    vertices = []
    # Iterate from 1 to n
    for i in range(1, n+1):
        # Append the current vertex to the list
        vertices.append(i)
    # Initialize a variable to store the minimum difference
    min_diff = 181
    # Initialize variables to store the optimal vertices
    v1, v2, v3 = 0, 0, 0
    # Iterate through all possible combinations of vertices
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # Calculate the angle between the current vertices
                angle = (vertices[i] - vertices[j]) * (vertices[k] - vertices[j])
                # Calculate the difference between the current angle and the needed angle
                diff = abs(angle - a)
                # If the difference is less than the minimum difference, update the minimum difference and the optimal vertices
                if diff < min_diff:
                    min_diff = diff
                    v1, v2, v3 = vertices[i], vertices[j], vertices[k]
    # Return the optimal vertices
    return v1, v2, v3


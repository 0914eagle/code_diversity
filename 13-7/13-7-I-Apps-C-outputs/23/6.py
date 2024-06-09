
def get_max_circumference(vertices):
    
    # Calculate the distance between each pair of vertices
    distances = []
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            dx = vertices[i][0] - vertices[j][0]
            dy = vertices[i][1] - vertices[j][1]
            distances.append(dx*dx + dy*dy)
    
    # Sort the distances in descending order
    distances.sort(reverse=True)
    
    # Calculate the sum of the distances
    sum_distances = sum(distances)
    
    # Calculate the maximum circumference
    max_circumference = 3.0 * sum_distances / (2.0 * (len(vertices) - 3))
    
    return max_circumference


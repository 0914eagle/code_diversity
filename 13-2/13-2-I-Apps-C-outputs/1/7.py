
def solve(shadow_walk, lydia_walk):
    # Calculate the distance between the two dogs at each point in their walks
    distances = []
    for i in range(len(shadow_walk)):
        for j in range(len(lydia_walk)):
            distances.append(calculate_distance(shadow_walk[i], lydia_walk[j]))
    
    # Find the minimum distance between the two dogs
    return min(distances)

def calculate_distance(point1, point2):
    # Calculate the Euclidean distance between two points
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


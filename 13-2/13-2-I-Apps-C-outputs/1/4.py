
def get_min_distance(shadow_walk, lydia_walk):
    # Calculate the distance between the two dogs at each point in their walks
    distances = []
    for i in range(len(shadow_walk)):
        for j in range(len(lydia_walk)):
            distances.append(get_distance(shadow_walk[i], lydia_walk[j]))
    
    # Return the minimum distance between the two dogs
    return min(distances)

def get_distance(point1, point2):
    # Calculate the Euclidean distance between two points
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

shadow_walk = [(0, 0), (10, 0)]
lydia_walk = [(30, 0), (15, 0)]
print(get_min_distance(shadow_walk, lydia_walk))


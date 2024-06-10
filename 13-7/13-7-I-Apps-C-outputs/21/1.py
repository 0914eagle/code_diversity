
import math

def get_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def get_tunnel_length(island_centers, palm_trees, k):
    # Initialize the minimum length of the tunnel as 0
    min_length = 0
    
    # Iterate through each pair of islands
    for i in range(len(island_centers)):
        for j in range(i + 1, len(island_centers)):
            # Get the distance between the centers of the two islands
            distance = get_distance(island_centers[i], island_centers[j])
            
            # Check if the distance is greater than the minimum length of the tunnel
            if distance > min_length:
                # Initialize a new minimum length for the tunnel
                min_length = distance
    
    # Iterate through each palm tree
    for tree in palm_trees:
        # Get the distance between the center of the island and the palm tree
        distance = get_distance(island_centers[tree[2]], (tree[0], tree[1]))
        
        # Check if the distance is greater than the minimum length of the tunnel
        if distance > min_length:
            # Initialize a new minimum length for the tunnel
            min_length = distance
    
    # Return the minimum length of the tunnel
    return min_length

def get_tunnel_length_fast(island_centers, palm_trees, k):
    # Initialize the minimum length of the tunnel as 0
    min_length = 0
    
    # Iterate through each pair of islands
    for i in range(len(island_centers)):
        for j in range(i + 1, len(island_centers)):
            # Get the distance between the centers of the two islands
            distance = get_distance(island_centers[i], island_centers[j])
            
            # Check if the distance is greater than the minimum length of the tunnel
            if distance > min_length:
                # Initialize a new minimum length for the tunnel
                min_length = distance
    
    # Iterate through each palm tree
    for tree in palm_trees:
        # Get the distance between the center of the island and the palm tree
        distance = get_distance(island_centers[tree[2]], (tree[0], tree[1]))
        
        # Check if the distance is greater than the minimum length of the tunnel
        if distance > min_length:
            # Initialize a new minimum length for the tunnel
            min_length = distance
    
    # Return the minimum length of the tunnel
    return min_length

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    island_centers = []
    palm_trees = []
    
    for i in range(n):
        x, y, r = map(int, input().split())
        island_centers.append((x, y))
    
    for i in range(m):
        x, y, h = map(int, input().split())
        palm_trees.append((x, y, h))
    
    print(get_tunnel_length(island_centers, palm_trees, k))


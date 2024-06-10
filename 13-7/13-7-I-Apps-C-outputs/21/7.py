
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_min_tunnel_length(island_centers, palm_trees, k):
    # Initialize the minimum tunnel length to 0
    min_tunnel_length = 0
    
    # Loop through each island center and palm tree
    for island_center in island_centers:
        for palm_tree in palm_trees:
            # Calculate the distance between the island center and the palm tree
            distance = get_distance(island_center[0], island_center[1], palm_tree[0], palm_tree[1])
            
            # If the distance is greater than the minimum tunnel length, update the minimum tunnel length
            if distance > min_tunnel_length:
                min_tunnel_length = distance
    
    # Return the minimum tunnel length
    return min_tunnel_length

def main():
    # Read the number of islands, palm trees, and k from stdin
    n, m, k = map(int, input().split())
    
    # Read the island centers and palm trees from stdin
    island_centers = []
    palm_trees = []
    for i in range(n):
        island_center = list(map(int, input().split()))
        island_centers.append(island_center)
    
    for i in range(m):
        palm_tree = list(map(int, input().split()))
        palm_trees.append(palm_tree)
    
    # Calculate the minimum tunnel length
    min_tunnel_length = get_min_tunnel_length(island_centers, palm_trees, k)
    
    # Print the minimum tunnel length
    print(min_tunnel_length)

if __name__ == '__main__':
    main()



import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_min_tunnel_length(islands, palm_trees, throw_ratio):
    # Initialize the minimum tunnel length to 0
    min_tunnel_length = 0
    
    # Loop through each island
    for island in islands:
        # Get the center and radius of the island
        island_center = (island[0], island[1])
        island_radius = island[2]
        
        # Loop through each palm tree
        for palm_tree in palm_trees:
            # Get the center and height of the palm tree
            palm_center = (palm_tree[0], palm_tree[1])
            palm_height = palm_tree[2]
            
            # Calculate the distance between the island center and the palm tree center
            distance = get_distance(island_center[0], island_center[1], palm_center[0], palm_center[1])
            
            # Calculate the maximum distance that can be thrown from the island center to the palm tree center
            max_throw_distance = island_radius * throw_ratio
            
            # If the distance is greater than the maximum throw distance, we need a tunnel
            if distance > max_throw_distance:
                # Calculate the length of the tunnel needed to connect the island center to the palm tree center
                tunnel_length = distance - max_throw_distance
                
                # If the tunnel length is greater than the current minimum tunnel length, update the minimum tunnel length
                if tunnel_length > min_tunnel_length:
                    min_tunnel_length = tunnel_length
    
    # Return the minimum tunnel length
    return min_tunnel_length

def main():
    # Read the number of islands, palm trees, and throw ratio from stdin
    n, m, k = map(int, input().split())
    
    # Read the coordinates of the islands from stdin
    islands = []
    for i in range(n):
        x, y, r = map(int, input().split())
        islands.append((x, y, r))
    
    # Read the coordinates of the palm trees from stdin
    palm_trees = []
    for i in range(m):
        x, y, h = map(int, input().split())
        palm_trees.append((x, y, h))
    
    # Call the get_min_tunnel_length function to get the minimum tunnel length
    min_tunnel_length = get_min_tunnel_length(islands, palm_trees, k)
    
    # Print the minimum tunnel length
    print(min_tunnel_length)

if __name__ == '__main__':
    main()


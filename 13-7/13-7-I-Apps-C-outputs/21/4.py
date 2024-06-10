
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_tunnel_length(islands, palm_trees, throw_ratio):
    # Initialize the minimum tunnel length to 0
    min_length = 0
    
    # Iterate over each island
    for i in range(len(islands)):
        # Get the center and radius of the current island
        center_x, center_y, radius = islands[i]
        
        # Find the closest palm tree to the center of the island
        closest_palm = find_closest_palm(palm_trees, center_x, center_y)
        
        # If the closest palm tree is not in the same island, we need to build a tunnel
        if closest_palm[2] != i:
            # Get the center and height of the closest palm tree
            palm_x, palm_y, palm_height = closest_palm
            
            # Calculate the distance between the center of the island and the palm tree
            distance = get_distance(center_x, center_y, palm_x, palm_y)
            
            # Calculate the maximum throwing distance based on the throw ratio and the palm height
            max_throw_distance = throw_ratio * palm_height
            
            # If the distance between the center of the island and the palm tree is greater than the maximum throwing distance, we need to build a tunnel
            if distance > max_throw_distance:
                # Calculate the length of the tunnel needed to connect the two islands
                tunnel_length = distance - max_throw_distance
                
                # If the tunnel length is greater than the current minimum length, update the minimum length
                if tunnel_length > min_length:
                    min_length = tunnel_length
    
    return min_length

def find_closest_palm(palm_trees, center_x, center_y):
    # Initialize the closest palm tree to the first palm tree in the list
    closest_palm = palm_trees[0]
    
    # Initialize the minimum distance to the distance between the center of the island and the first palm tree
    min_distance = get_distance(center_x, center_y, closest_palm[0], closest_palm[1])
    
    # Iterate over each palm tree
    for palm in palm_trees:
        # Calculate the distance between the center of the island and the current palm tree
        distance = get_distance(center_x, center_y, palm[0], palm[1])
        
        # If the distance is less than the minimum distance, update the minimum distance and the closest palm tree
        if distance < min_distance:
            min_distance = distance
            closest_palm = palm
    
    return closest_palm

def main():
    # Read the number of islands, palm trees, and throw ratio from stdin
    n, m, throw_ratio = map(int, input().split())
    
    # Read the coordinates and radius of the islands from stdin
    islands = []
    for i in range(n):
        x, y, r = map(int, input().split())
        islands.append((x, y, r))
    
    # Read the coordinates and height of the palm trees from stdin
    palm_trees = []
    for i in range(m):
        x, y, h = map(int, input().split())
        palm_trees.append((x, y, h))
    
    # Calculate the minimum length of a tunnel needed for a courier system
    min_length = get_tunnel_length(islands, palm_trees, throw_ratio)
    
    # Print the minimum length of the tunnel
    print(min_length)

if __name__ == '__main__':
    main()


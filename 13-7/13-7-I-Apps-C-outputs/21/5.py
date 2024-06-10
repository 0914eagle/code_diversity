
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_min_tunnel_length(islands, palm_trees, throwing_ratio):
    # Initialize the minimum tunnel length to 0
    min_tunnel_length = 0
    
    # Iterate over each pair of islands
    for i in range(len(islands)):
        for j in range(i+1, len(islands)):
            # Get the centers and radii of the two islands
            island1_center = islands[i][:2]
            island2_center = islands[j][:2]
            island1_radius = islands[i][2]
            island2_radius = islands[j][2]
            
            # Check if the two islands are not intersecting
            if get_distance(island1_center[0], island1_center[1], island2_center[0], island2_center[1]) > island1_radius + island2_radius:
                # Get the closest palm tree on each island
                closest_palm_tree1 = get_closest_palm_tree(palm_trees, island1_center)
                closest_palm_tree2 = get_closest_palm_tree(palm_trees, island2_center)
                
                # Check if the two palm trees are not in the same island
                if closest_palm_tree1[0] != closest_palm_tree2[0]:
                    # Calculate the distance between the two palm trees
                    distance = get_distance(closest_palm_tree1[1][0], closest_palm_tree1[1][1], closest_palm_tree2[1][0], closest_palm_tree2[1][1])
                    
                    # Calculate the minimum tunnel length needed to connect the two islands
                    min_tunnel_length = max(min_tunnel_length, distance - throwing_ratio * closest_palm_tree1[1][2])
    
    return min_tunnel_length

def get_closest_palm_tree(palm_trees, island_center):
    closest_distance = float('inf')
    closest_palm_tree = None
    
    for palm_tree in palm_trees:
        distance = get_distance(palm_tree[0], palm_tree[1], island_center[0], island_center[1])
        if distance < closest_distance:
            closest_distance = distance
            closest_palm_tree = palm_tree
    
    return closest_palm_tree

def main():
    # Read the input data
    num_islands, num_palm_trees, throwing_ratio = map(int, input().split())
    islands = [list(map(int, input().split())) for _ in range(num_islands)]
    palm_trees = [list(map(int, input().split())) for _ in range(num_palm_trees)]
    
    # Find the minimum tunnel length
    min_tunnel_length = get_min_tunnel_length(islands, palm_trees, throwing_ratio)
    
    # Print the result
    print(min_tunnel_length)

if __name__ == '__main__':
    main()


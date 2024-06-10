
import math

def get_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def get_min_tunnel_length(islands, palm_trees, k):
    # Initialize the minimum tunnel length to 0
    min_tunnel_length = 0
    
    # Loop through each pair of islands
    for i in range(len(islands)):
        for j in range(i + 1, len(islands)):
            # Get the distance between the two islands
            distance = get_distance(islands[i], islands[j])
            
            # If the distance is greater than the minimum tunnel length, continue to the next pair of islands
            if distance > min_tunnel_length:
                continue
            
            # Loop through each palm tree on island i
            for tree1 in palm_trees[i]:
                # Get the distance from the palm tree to island j
                distance_to_island = get_distance(tree1, islands[j])
                
                # If the distance from the palm tree to island j is greater than the minimum tunnel length, continue to the next palm tree
                if distance_to_island > min_tunnel_length:
                    continue
                
                # Loop through each palm tree on island j
                for tree2 in palm_trees[j]:
                    # Get the distance between the two palm trees
                    distance_between_trees = get_distance(tree1, tree2)
                    
                    # If the distance between the two palm trees is less than or equal to the minimum tunnel length, continue to the next pair of palm trees
                    if distance_between_trees <= min_tunnel_length:
                        continue
                    
                    # Calculate the minimum tunnel length needed to connect the two palm trees
                    min_tunnel_length = max(min_tunnel_length, distance_to_island + distance_between_trees - k * tree1[2])
    
    return min_tunnel_length

def main():
    # Read the number of islands, palm trees, and k
    n, m, k = map(int, input().split())
    
    # Read the coordinates of the islands
    islands = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        islands.append((x, y, r))
    
    # Read the coordinates and heights of the palm trees
    palm_trees = [[] for _ in range(n)]
    for _ in range(m):
        x, y, h = map(int, input().split())
        palm_trees[x // 1000].append((x % 1000, y, h))
    
    # Calculate the minimum tunnel length
    min_tunnel_length = get_min_tunnel_length(islands, palm_trees, k)
    
    # Print the minimum tunnel length
    print(min_tunnel_length)

if __name__ == '__main__':
    main()


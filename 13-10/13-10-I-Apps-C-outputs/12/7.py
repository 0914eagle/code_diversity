
import math

def get_tree_pairs(N, L, W):
    # Calculate the distance between each tree pair
    distance = (L - W) / (N - 1)
    
    # Initialize a list to store the positions of the tree pairs
    positions = []
    
    # Loop through each tree pair
    for i in range(N):
        # Calculate the position of the tree pair
        position = (i * distance) + (W / 2)
        
        # Add the position to the list
        positions.append(position)
    
    return positions

def calculate_total_distance(positions):
    # Initialize a variable to store the total distance
    total_distance = 0
    
    # Loop through each tree pair
    for i in range(len(positions) - 1):
        # Calculate the distance between each tree pair
        distance = math.sqrt((positions[i + 1] - positions[i]) ** 2 + (W / 2) ** 2)
        
        # Add the distance to the total distance
        total_distance += distance
    
    return total_distance

def main():
    N, L, W = map(int, input().split())
    positions = get_tree_pairs(N, L, W)
    total_distance = calculate_total_distance(positions)
    print(total_distance)

if __name__ == '__main__':
    main()


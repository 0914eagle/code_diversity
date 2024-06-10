
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def find_leash_length(toy_coordinates, tree_coordinates):
    # Initialize the leash length to 0
    leash_length = 0
    
    # Loop through the toy coordinates and add the distance to the leash length
    for i in range(len(toy_coordinates)):
        leash_length += distance(toy_coordinates[i][0], toy_coordinates[i][1], 0, 0)
    
    # If there are trees, loop through the tree coordinates and add the distance to the leash length
    if tree_coordinates:
        for i in range(len(tree_coordinates)):
            leash_length += distance(tree_coordinates[i][0], tree_coordinates[i][1], 0, 0)
    
    # Return the leash length
    return leash_length

def main():
    # Read the number of toys and trees
    n, m = map(int, input().split())
    
    # Read the toy coordinates
    toy_coordinates = []
    for i in range(n):
        x, y = map(int, input().split())
        toy_coordinates.append((x, y))
    
    # Read the tree coordinates
    tree_coordinates = []
    for i in range(m):
        x, y = map(int, input().split())
        tree_coordinates.append((x, y))
    
    # Find the leash length
    leash_length = find_leash_length(toy_coordinates, tree_coordinates)
    
    # Print the leash length
    print(round(leash_length, 2))

if __name__ == '__main__':
    main()


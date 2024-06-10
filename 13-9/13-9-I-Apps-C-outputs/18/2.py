
import math

def get_toys_coordinates(n):
    toys = []
    for i in range(n):
        x, y = map(int, input().split())
        toys.append((x, y))
    return toys

def get_trees_coordinates(m):
    trees = []
    for i in range(m):
        x, y = map(int, input().split())
        trees.append((x, y))
    return trees

def get_leash_length(toys, trees):
    # Calculate the distance from Spot's starting position to the first toy
    dist_to_first_toy = math.sqrt((toys[0][0] - 0) ** 2 + (toys[0][1] - 0) ** 2)
    
    # Calculate the distance from Spot's starting position to the next toy
    dist_to_next_toy = math.sqrt((toys[1][0] - 0) ** 2 + (toys[1][1] - 0) ** 2)
    
    # Calculate the length of the leash needed to reach the first toy
    leash_length = dist_to_first_toy + dist_to_next_toy
    
    # If there are trees in the park, calculate the distance from Spot's starting position to the nearest tree
    if len(trees) > 0:
        dist_to_tree = min([math.sqrt((trees[i][0] - 0) ** 2 + (trees[i][1] - 0) ** 2) for i in range(len(trees))])
        
        # If the distance to the tree is less than the distance to the first toy, increase the leash length to account for the tree
        if dist_to_tree < dist_to_first_toy:
            leash_length += dist_to_tree
    
    return leash_length

def main():
    n, m = map(int, input().split())
    toys = get_toys_coordinates(n)
    trees = get_trees_coordinates(m)
    leash_length = get_leash_length(toys, trees)
    print(f"{leash_length:.2f}")

if __name__ == '__main__':
    main()


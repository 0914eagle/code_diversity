
import math

def get_toys(n, toys):
    # Initialize the list of toys and the current location of Spot
    toy_list = []
    spot_x = 0
    spot_y = 0
    
    # Loop through the toys and add them to the list
    for i in range(n):
        toy_x, toy_y = map(int, toys[i].split())
        toy_list.append((toy_x, toy_y))
    
    # Return the list of toys and the current location of Spot
    return toy_list, spot_x, spot_y

def get_trees(m, trees):
    # Initialize the list of trees
    tree_list = []
    
    # Loop through the trees and add them to the list
    for i in range(m):
        tree_x, tree_y = map(int, trees[i].split())
        tree_list.append((tree_x, tree_y))
    
    # Return the list of trees
    return tree_list

def get_distance(spot_x, spot_y, toy_x, toy_y):
    # Calculate the distance between Spot and the toy
    distance = math.sqrt((spot_x - toy_x)**2 + (spot_y - toy_y)**2)
    
    # Return the distance
    return distance

def get_leash_length(toy_list, tree_list, spot_x, spot_y):
    # Initialize the leash length
    leash_length = 0
    
    # Loop through the toys and calculate the distance between Spot and each toy
    for toy_x, toy_y in toy_list:
        distance = get_distance(spot_x, spot_y, toy_x, toy_y)
        
        # Check if the distance is longer than the current leash length
        if distance > leash_length:
            leash_length = distance
    
    # Loop through the trees and calculate the distance between Spot and each tree
    for tree_x, tree_y in tree_list:
        distance = get_distance(spot_x, spot_y, tree_x, tree_y)
        
        # Check if the distance is longer than the current leash length
        if distance > leash_length:
            leash_length = distance
    
    # Return the leash length
    return leash_length

def main():
    # Read the input
    n, m = map(int, input().split())
    toys = [input() for i in range(n)]
    trees = [input() for i in range(m)]
    
    # Get the list of toys and the current location of Spot
    toy_list, spot_x, spot_y = get_toys(n, toys)
    
    # Get the list of trees
    tree_list = get_trees(m, trees)
    
    # Calculate the leash length
    leash_length = get_leash_length(toy_list, tree_list, spot_x, spot_y)
    
    # Print the leash length
    print(f"{leash_length:.2f}")

if __name__ == '__main__':
    main()


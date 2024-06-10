
def get_minimum_inspectors(num_trees, distance):
    # Initialize a list to store the inspected trees
    inspected_trees = [False] * (num_trees + 1)
    
    # Initialize the minimum number of inspectors to deploy
    min_inspectors = 0
    
    # Iterate through each tree
    for tree in range(1, num_trees + 1):
        # Check if the tree has not been inspected yet
        if not inspected_trees[tree]:
            # Increment the minimum number of inspectors to deploy
            min_inspectors += 1
            # Mark the tree and its neighbors as inspected
            for neighbor in range(tree - distance, tree + distance + 1):
                if 1 <= neighbor <= num_trees:
                    inspected_trees[neighbor] = True
    
    return min_inspectors

def main():
    # Read the input from stdin
    num_trees, distance = map(int, input().split())
    
    # Find the minimum number of inspectors to deploy
    min_inspectors = get_minimum_inspectors(num_trees, distance)
    
    # Print the result
    print(min_inspectors)

if __name__ == '__main__':
    main()


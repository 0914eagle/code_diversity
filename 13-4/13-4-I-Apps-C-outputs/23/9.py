
def is_possible(n, parent, x):
    # Initialize the color and weight of the root vertex as white and 0
    color = ["white"] * (n + 1)
    weight = [0] * (n + 1)
    
    # Set the color and weight of the root vertex
    color[1] = "white"
    weight[1] = 0
    
    # Iterate through the vertices in the tree
    for i in range(2, n + 1):
        # Get the parent of the current vertex
        p = parent[i]
        
        # If the parent has the same color as the current vertex, set the current vertex's color to black
        if color[p] == color[i]:
            color[i] = "black"
        
        # Set the current vertex's weight to the difference between its parent's weight and its own weight
        weight[i] = weight[p] - x[i]
    
    # Check if the total weight of the vertices with the same color as the root vertex is equal to X_1
    if weight[1] != x[1]:
        return "IMPOSSIBLE"
    
    # Check if the total weight of the vertices with the same color as the root vertex is equal to X_i for all i
    for i in range(2, n + 1):
        if weight[i] != x[i]:
            return "IMPOSSIBLE"
    
    # If all conditions are satisfied, return POSSIBLE
    return "POSSIBLE"

def main():
    n = int(input())
    parent = [int(i) for i in input().split()]
    x = [int(i) for i in input().split()]
    print(is_possible(n, parent, x))

if __name__ == '__main__':
    main()


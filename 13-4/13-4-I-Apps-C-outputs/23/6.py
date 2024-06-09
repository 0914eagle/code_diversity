
def is_possible(n, parents, x):
    # Initialize the color and weight of each vertex as None
    colors = [None] * (n + 1)
    weights = [0] * (n + 1)
    
    # Set the color and weight of the root vertex (Vertex 1)
    colors[1] = "white"
    weights[1] = x[1]
    
    # Iterate through the vertices in the order of their depth in the tree
    for i in range(2, n + 1):
        # Get the parent of the current vertex
        parent = parents[i]
        
        # If the parent has not been colored yet, color it with the opposite color of the current vertex
        if colors[parent] is None:
            colors[parent] = "white" if colors[i] == "black" else "black"
        
        # If the parent has already been colored, check if the color is the same as the current vertex
        else:
            if colors[parent] == colors[i]:
                return False
        
        # Set the weight of the current vertex to the sum of its weight and the weight of its parent
        weights[i] = weights[parent] + x[i]
    
    # Check if the total weight of the vertices with the same color as the root vertex is equal to the root vertex's weight
    if weights[1] != x[1]:
        return False
    
    # If all the conditions are met, return True
    return True

def main():
    n = int(input())
    parents = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    print("POSSIBLE" if is_possible(n, parents, x) else "IMPOSSIBLE")

if __name__ == '__main__':
    main()


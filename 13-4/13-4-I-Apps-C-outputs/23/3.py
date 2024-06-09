
def is_possible(n, parents, x):
    # Initialize the color and weight of each vertex as None
    colors = [None] * (n + 1)
    weights = [0] * (n + 1)
    
    # Set the color and weight of the root vertex (Vertex 1)
    colors[1] = "white"
    weights[1] = x[1]
    
    # Iterate through the vertices in topological order
    for i in range(2, n + 1):
        # Get the parent of the current vertex
        parent = parents[i]
        
        # If the parent has already been colored, copy its color and weight
        if colors[parent] is not None:
            colors[i] = colors[parent]
            weights[i] = weights[parent]
        # If the parent has not been colored, color it with the opposite color of its child
        else:
            colors[i] = "white" if colors[i] == "black" else "black"
            weights[i] = x[i]
    
    # Check if the total weight of the vertices with the same color as the root vertex is equal to X_1
    if weights[1] != x[1]:
        return False
    
    # Iterate through the vertices in topological order
    for i in range(2, n + 1):
        # Get the parent of the current vertex
        parent = parents[i]
        
        # If the parent has already been colored, check if the total weight of the vertices with the same color as the current vertex is equal to X_i
        if colors[parent] is not None:
            if weights[i] != x[i]:
                return False
        # If the parent has not been colored, color it with the opposite color of its child
        else:
            colors[i] = "white" if colors[i] == "black" else "black"
            weights[i] = x[i]
    
    # If all vertices have been colored and the total weight of the vertices with the same color as the root vertex is equal to X_1, return True
    return True

def main():
    n = int(input())
    parents = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    if is_possible(n, parents, x):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()


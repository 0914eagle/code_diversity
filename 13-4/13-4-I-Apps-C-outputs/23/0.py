
def is_possible(N, parents, X):
    # Initialize a dictionary to store the color and weight of each vertex
    colors = {}
    weights = {}
    
    # Set the color and weight of the root vertex (Vertex 1)
    colors[1] = "white"
    weights[1] = X[1]
    
    # Iterate through the remaining vertices
    for i in range(2, N+1):
        # Get the parent of the current vertex
        parent = parents[i]
        
        # If the parent has the same color as the current vertex, set the current vertex's color to the opposite color
        if colors[parent] == colors[i]:
            colors[i] = "white" if colors[i] == "black" else "black"
        # Otherwise, set the current vertex's color to the same color as its parent
        else:
            colors[i] = colors[parent]
        
        # Set the current vertex's weight to the difference between its parent's weight and its own weight
        weights[i] = weights[parent] - X[i]
    
    # Check if the total weight of the vertices with the same color as Vertex 1 is equal to X[1]
    if weights[1] != X[1]:
        return "IMPOSSIBLE"
    
    # If the allocation is possible, return "POSSIBLE"
    return "POSSIBLE"

def main():
    N = int(input())
    parents = list(map(int, input().split()))
    X = list(map(int, input().split()))
    print(is_possible(N, parents, X))

if __name__ == '__main__':
    main()



def is_possible(N, P, X):
    # Initialize the colors and weights of the vertices
    colors = [""] * (N + 1)
    weights = [0] * (N + 1)
    
    # Set the color and weight of the root vertex (Vertex 1)
    colors[1] = "white"
    weights[1] = X[1]
    
    # Loop through the remaining vertices
    for i in range(2, N + 1):
        # Get the parent of the current vertex
        parent = P[i]
        
        # If the current vertex has the same color as its parent, set its color to the other color
        if colors[parent] == colors[i]:
            colors[i] = "black" if colors[parent] == "white" else "white"
        
        # Set the weight of the current vertex to the sum of its weight and the weight of its parent
        weights[i] = weights[parent] + X[i]
    
    # Check if the total weight of the vertices with the same color as the root vertex is equal to X[1]
    if weights[1] != X[1]:
        return "IMPOSSIBLE"
    
    # Loop through the remaining vertices
    for i in range(2, N + 1):
        # If the total weight of the vertices with the same color as the current vertex is not equal to X[i], return IMPOSSIBLE
        if weights[i] != X[i]:
            return "IMPOSSIBLE"
    
    # If all vertices have been checked and the condition has been satisfied for all of them, return POSSIBLE
    return "POSSIBLE"

def main():
    # Read the input from stdin
    N = int(input())
    P = list(map(int, input().split()))
    X = list(map(int, input().split()))
    
    # Call the is_possible function and print the result
    print(is_possible(N, P, X))

if __name__ == '__main__':
    main()


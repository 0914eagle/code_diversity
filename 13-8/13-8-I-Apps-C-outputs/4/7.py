
def is_possible(N, P, X):
    # Initialize a list to store the colors and weights of each vertex
    colors = [None] * (N + 1)
    weights = [0] * (N + 1)
    
    # Set the color and weight of the root vertex (Vertex 1)
    colors[1] = "white"
    weights[1] = X[1]
    
    # Iterate through the remaining vertices
    for i in range(2, N + 1):
        # Get the parent of the current vertex
        parent = P[i]
        
        # If the current vertex has a white parent, set its color to black
        if colors[parent] == "white":
            colors[i] = "black"
        # If the current vertex has a black parent, set its color to white
        else:
            colors[i] = "white"
        
        # Set the weight of the current vertex to the difference between its X value and the X value of its parent
        weights[i] = X[i] - X[parent]
    
    # Check if the total weight of the vertices with the same color as Vertex 1 is equal to its X value
    if weights[1] != X[1]:
        return "IMPOSSIBLE"
    
    # Check if the total weight of the vertices with the same color as each vertex is equal to its X value
    for i in range(2, N + 1):
        if weights[i] != X[i]:
            return "IMPOSSIBLE"
    
    # If all vertices have been processed and the condition is satisfied, return "POSSIBLE"
    return "POSSIBLE"

def main():
    N = int(input())
    P = list(map(int, input().split()))
    X = list(map(int, input().split()))
    print(is_possible(N, P, X))

if __name__ == '__main__':
    main()


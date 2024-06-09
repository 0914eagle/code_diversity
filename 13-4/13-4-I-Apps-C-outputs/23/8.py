
def is_possible(N, P, X):
    # Initialize a dictionary to store the color and weight of each vertex
    colors = {}
    weights = {}
    
    # Set the color and weight of the root vertex (Vertex 1)
    colors[1] = "white"
    weights[1] = X[1]
    
    # Iterate through the remaining vertices (Vertex 2 to N)
    for i in range(2, N+1):
        # Get the parent of the current vertex
        parent = P[i-1]
        
        # If the parent has the same color as the current vertex, set the color of the current vertex to the opposite color
        if colors[parent] == colors[i]:
            colors[i] = "white" if colors[i] == "black" else "black"
        
        # Set the weight of the current vertex to the difference between the weight of its parent and the weight of the current vertex
        weights[i] = weights[parent] - X[i]
    
    # Check if the weight of all vertices is non-negative
    for i in range(1, N+1):
        if weights[i] < 0:
            return False
    
    return True

def main():
    N = int(input())
    P = list(map(int, input().split()))
    X = list(map(int, input().split()))
    
    if is_possible(N, P, X):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()


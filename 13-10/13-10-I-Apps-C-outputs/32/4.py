
def solve(N, parent, X):
    # Initialize the colors and weights for each vertex
    colors = ["white"] * (N + 1)
    weights = [0] * (N + 1)
    
    # Set the color and weight for the root vertex (Vertex 1)
    colors[1] = "black"
    weights[1] = X[1]
    
    # Iterate through the vertices in topological order
    for i in range(2, N + 1):
        # Get the parent of the current vertex
        parent_idx = parent[i]
        
        # If the current vertex is the root of a subtree,
        # set its color and weight based on the condition
        if parent_idx == i - 1:
            colors[i] = "black" if colors[parent_idx] == "white" else "white"
            weights[i] = X[i]
        # Otherwise, set its color and weight based on the parent's color and weight
        else:
            colors[i] = colors[parent_idx]
            weights[i] = weights[parent_idx] + X[i]
    
    # Check if the condition is satisfied for all vertices
    for i in range(1, N + 1):
        if weights[i] != X[i]:
            return "IMPOSSIBLE"
    
    return "POSSIBLE"

def main():
    N = int(input())
    parent = list(map(int, input().split()))
    X = list(map(int, input().split()))
    print(solve(N, parent, X))

if __name__ == '__main__':
    main()


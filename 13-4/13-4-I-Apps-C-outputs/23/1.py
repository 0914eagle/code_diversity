
def is_possible(n, parents, x_sequence):
    # Initialize a dictionary to store the color and weight of each vertex
    colors = {}
    weights = {}
    
    # Set the color and weight of the root vertex (Vertex 1)
    colors[1] = "white"
    weights[1] = x_sequence[1]
    
    # Iterate through the remaining vertices (Vertices 2 to N)
    for i in range(2, n + 1):
        # Get the parent of the current vertex
        parent = parents[i - 1]
        
        # If the parent has the same color as the current vertex, set the current vertex's color to the opposite color
        if colors[parent] == colors[i]:
            colors[i] = "white" if colors[i] == "black" else "black"
        # If the parent has a different color than the current vertex, set the current vertex's color to the same color as the parent
        else:
            colors[i] = colors[parent]
        
        # Set the current vertex's weight to the difference between its parent's weight and its own weight
        weights[i] = weights[parent] - x_sequence[i]
    
    # Check if all vertices have a non-negative weight
    for i in range(1, n + 1):
        if weights[i] < 0:
            return False
    
    return True

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    x_sequence = list(map(int, input().split()))
    
    if is_possible(n, parents, x_sequence):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()


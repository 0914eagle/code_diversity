
def is_possible(n, parents, x_sequence):
    # Initialize a dictionary to store the color and weight of each vertex
    colors = {}
    weights = {}
    
    # Set the color and weight of the root vertex (Vertex 1)
    colors[1] = "white"
    weights[1] = x_sequence[1]
    
    # Iterate through the remaining vertices
    for i in range(2, n+1):
        # Get the parent of the current vertex
        parent = parents[i-1]
        
        # If the parent has the same color as the current vertex, set the current vertex's color to the opposite color
        if colors[parent] == colors[i]:
            colors[i] = "white" if colors[i] == "black" else "black"
        # If the parent has a different color than the current vertex, set the current vertex's color to the same color as the parent
        else:
            colors[i] = colors[parent]
        
        # Set the weight of the current vertex to the difference between its X value and the weight of its parent
        weights[i] = x_sequence[i] - weights[parent]
    
    # Check if the total weight of the vertices with the same color as Vertex 1 is equal to its X value
    if weights[1] != x_sequence[1]:
        return False
    
    # Check if the total weight of the vertices with the same color as each vertex is equal to its X value
    for i in range(2, n+1):
        if weights[i] != x_sequence[i]:
            return False
    
    # If all conditions are met, return True
    return True

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    x_sequence = list(map(int, input().split()))
    print("POSSIBLE" if is_possible(n, parents, x_sequence) else "IMPOSSIBLE")

if __name__ == '__main__':
    main()



def is_possible(n, parent, x):
    # Initialize a dictionary to store the color and weight of each vertex
    colors = {}
    weights = {}
    
    # Set the color and weight of the root vertex (Vertex 1)
    colors[1] = "white"
    weights[1] = x[1]
    
    # Iterate through the remaining vertices
    for i in range(2, n+1):
        # Get the parent of the current vertex
        parent_i = parent[i-1]
        
        # If the parent has the same color as the current vertex, set the current vertex's color to the opposite color
        if colors[parent_i] == colors[i]:
            colors[i] = "white" if colors[i] == "black" else "black"
        
        # Set the current vertex's weight to the difference between its parent's weight and its X value
        weights[i] = weights[parent_i] - x[i]
        
        # If the current vertex's weight is negative, return false
        if weights[i] < 0:
            return False
    
    # If all vertices have valid colors and weights, return true
    return True

def main():
    n = int(input())
    parent = list(map(int, input().split()))
    x = list(map(int, input().split()))
    print("POSSIBLE" if is_possible(n, parent, x) else "IMPOSSIBLE")

if __name__ == '__main__':
    main()


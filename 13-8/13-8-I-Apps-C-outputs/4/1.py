
def is_possible(n, parents, x_sequence):
    # Initialize a dictionary to store the color and weight of each vertex
    colors = {}
    weights = {}
    
    # Set the color of the root vertex to white
    colors[1] = "white"
    weights[1] = x_sequence[1]
    
    # Iterate through the vertices in the tree
    for i in range(2, n+1):
        # Get the parent of the current vertex
        parent = parents[i]
        
        # If the current vertex has the same color as its parent, set its color to black
        if colors[parent] == colors[i]:
            colors[i] = "black"
        
        # Set the weight of the current vertex to the difference between its weight and the weight of its parent
        weights[i] = x_sequence[i] - weights[parent]
    
    # Check if the total weight of the vertices with the same color as the root vertex is equal to the weight of the root vertex
    if weights[1] != x_sequence[1]:
        return "IMPOSSIBLE"
    
    # Check if the total weight of the vertices with the same color as the root vertex is equal to the weight of the root vertex
    for i in range(2, n+1):
        if colors[i] == colors[1] and weights[i] != weights[1]:
            return "IMPOSSIBLE"
    
    return "POSSIBLE"

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    x_sequence = list(map(int, input().split()))
    print(is_possible(n, parents, x_sequence))

if __name__ == '__main__':
    main()


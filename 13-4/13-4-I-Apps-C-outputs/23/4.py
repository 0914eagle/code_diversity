
def is_possible(n, parents, x):
    # Initialize the color and weight of each vertex as None
    color = [None] * (n + 1)
    weight = [0] * (n + 1)
    
    # Set the color and weight of the root vertex (1)
    color[1] = "white"
    weight[1] = x[1]
    
    # Iterate through the vertices in topological order
    for i in range(2, n + 1):
        # Get the parent of the current vertex
        parent = parents[i]
        
        # If the parent has not been colored, color it with the opposite color of the current vertex
        if color[parent] is None:
            color[parent] = "white" if color[i] == "black" else "black"
        
        # If the parent has already been colored, check if the color is the same as the current vertex
        else:
            if color[parent] == color[i]:
                return False
        
        # Update the weight of the parent with the weight of the current vertex
        weight[parent] += weight[i]
    
    # Check if the weight of the root vertex is equal to the total weight of the tree
    if weight[1] != sum(weight[2:]) + x[1]:
        return False
    
    # If all the vertices have been colored and the weight of the root vertex is correct, return True
    return True

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    x = list(map(int, input().split()))
    print("POSSIBLE" if is_possible(n, parents, x) else "IMPOSSIBLE")

if __name__ == '__main__':
    main()


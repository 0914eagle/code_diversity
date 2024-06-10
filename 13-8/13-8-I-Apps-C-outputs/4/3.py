
def is_possible(n, parent, x):
    # Initialize the color and weight of vertex 1 to white and 0, respectively
    color = [0] * (n + 1)
    weight = [0] * (n + 1)
    color[1] = 0
    weight[1] = 0
    
    # Loop through the vertices 2 to N
    for i in range(2, n + 1):
        # Get the parent of vertex i
        parent_i = parent[i - 1]
        
        # If the parent of vertex i is white, set its color to black and its weight to X_i
        if color[parent_i] == 0:
            color[i] = 1
            weight[i] = x[i - 1]
        
        # If the parent of vertex i is black, set its color to white and its weight to X_i - X_parent
        else:
            color[i] = 0
            weight[i] = x[i - 1] - x[parent_i - 1]
    
    # Check if the total weight of the vertices with the same color as vertex 1 is X_1
    if weight[1] != x[0]:
        return "IMPOSSIBLE"
    
    # Loop through the vertices 2 to N and check if the total weight of the vertices with the same color as each vertex is X_i
    for i in range(2, n + 1):
        if weight[i] != x[i - 1]:
            return "IMPOSSIBLE"
    
    # If all conditions are satisfied, return POSSIBLE
    return "POSSIBLE"

def main():
    n = int(input())
    parent = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    print(is_possible(n, parent, x))

if __name__ == '__main__':
    main()


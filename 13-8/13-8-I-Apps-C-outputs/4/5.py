
def is_possible(N, parent, X):
    # Initialize the color and weight of the root vertex as white and 0
    color = ["white"] * (N + 1)
    weight = [0] * (N + 1)
    
    # Loop through all vertices except the root vertex
    for i in range(2, N + 1):
        # Get the parent of the current vertex
        p = parent[i - 1]
        
        # If the current vertex has a different color than its parent, set its color to black
        if color[i] != color[p]:
            color[i] = "black"
        
        # Set the weight of the current vertex to the difference between its X value and the sum of the weights of its children
        weight[i] = X[i - 1] - sum(weight[j] for j in range(i + 1, N + 1) if parent[j - 1] == i)
    
    # Check if the weight of the root vertex is 0
    if weight[1] != 0:
        return "IMPOSSIBLE"
    
    # Check if the weight of all other vertices is non-negative
    for i in range(2, N + 1):
        if weight[i] < 0:
            return "IMPOSSIBLE"
    
    # If all conditions are satisfied, return POSSIBLE
    return "POSSIBLE"

def main():
    N, parent, X = read_input()
    print(is_possible(N, parent, X))

def read_input():
    N = int(input())
    parent = [int(i) for i in input().split()]
    X = [int(i) for i in input().split()]
    return N, parent, X

if __name__ == '__main__':
    main()


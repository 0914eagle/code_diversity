
import sys

def get_input():
    N = int(input())
    parent = [int(i) for i in input().split()]
    X = [int(i) for i in input().split()]
    return N, parent, X

def is_possible(N, parent, X):
    # Initialize the color and weight of each vertex to be white and 0
    color = [0] * (N + 1)
    weight = [0] * (N + 1)
    
    # Set the color and weight of the root vertex (Vertex 1) to be white and X[1]
    color[1] = 1
    weight[1] = X[1]
    
    # Iterate through the vertices in the tree, starting from the second vertex
    for i in range(2, N + 1):
        # Get the parent of the current vertex
        parent_idx = parent[i]
        
        # If the parent vertex has the same color as the current vertex, update the weight of the parent vertex
        if color[parent_idx] == color[i]:
            weight[parent_idx] += weight[i]
        
        # If the weight of the current vertex is not equal to X[i], it is not possible to satisfy the condition
        if weight[i] != X[i]:
            return False
        
        # If the current vertex is the root of a subtree, set its color to the opposite of its parent
        if parent_idx == 0:
            color[i] = 1 - color[parent_idx]
        
    return True

def main():
    N, parent, X = get_input()
    if is_possible(N, parent, X):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()



import sys

def get_input():
    N = int(input())
    P = [int(x) for x in input().split()]
    X = [int(x) for x in input().split()]
    return N, P, X

def is_possible(N, P, X):
    # Initialize the color and weight of the root vertex (Vertex 1)
    color = [0] * (N+1)
    weight = [0] * (N+1)
    color[1] = 1
    weight[1] = X[1]
    
    for i in range(2, N+1):
        # Set the color of the current vertex to the opposite color of its parent
        color[i] = 1 - color[P[i]]
        # Set the weight of the current vertex to the difference between its weight and the weight of its parent
        weight[i] = weight[P[i]] - X[i]
    
    # Check if the total weight of the vertices with the same color as the root vertex is equal to its weight
    if weight[1] != X[1]:
        return False
    
    # Check if the total weight of the vertices with the same color as the current vertex is equal to its weight
    for i in range(2, N+1):
        if weight[i] != X[i]:
            return False
    
    return True

def main():
    N, P, X = get_input()
    if is_possible(N, P, X):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()



def get_input():
    N = int(input())
    parent = [int(i) for i in input().split()]
    X = [int(i) for i in input().split()]
    return N, parent, X

def is_possible(N, parent, X):
    # Initialize the colors and weights of the vertices
    colors = [-1] * (N + 1)
    weights = [0] * (N + 1)
    colors[1] = 0
    weights[1] = X[1]
    
    # DFS to assign colors and weights to the vertices
    for i in range(2, N + 1):
        if colors[i] == -1:
            colors[i], weights[i] = dfs(i, parent, colors, weights, X)
    
    # Check if the condition is satisfied for all vertices
    for i in range(1, N + 1):
        if weights[i] != X[i]:
            return False
    return True

def dfs(i, parent, colors, weights, X):
    # Assign a color to the current vertex
    colors[i] = 1 - colors[parent[i]]
    
    # Assign a weight to the current vertex
    weights[i] = weights[parent[i]] + X[i]
    
    # Recursively assign colors and weights to the children of the current vertex
    for j in range(1, N + 1):
        if parent[j] == i:
            colors[j], weights[j] = dfs(j, parent, colors, weights, X)
    
    return colors[i], weights[i]

if __name__ == '__main__':
    N, parent, X = get_input()
    print("POSSIBLE" if is_possible(N, parent, X) else "IMPOSSIBLE")



def dfs(node, parent, color, weight, colors, weights, X, N):
    if node == 1:
        colors[node] = color
        weights[node] = weight
    else:
        colors[node] = 1 - color
        weights[node] = X[node] - weight
    
    for i in range(1, N+1):
        if P[i] == node:
            dfs(i, node, colors[node], weights[node], colors, weights, X, N)

def is_possible(X, N):
    P = [0] * (N+1)
    colors = [0] * (N+1)
    weights = [0] * (N+1)
    
    for i in range(2, N+1):
        P[i] = int(input())
    
    dfs(1, 0, 0, 0, colors, weights, X, N)
    
    for i in range(1, N+1):
        if colors[i] != 0 and weights[i] != X[i]:
            return "IMPOSSIBLE"
    
    return "POSSIBLE"

if __name__ == '__main__':
    N = int(input())
    X = [0] * (N+1)
    for i in range(1, N+1):
        X[i] = int(input())
    print(is_possible(X, N))


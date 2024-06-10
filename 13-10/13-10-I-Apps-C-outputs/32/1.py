
def get_input():
    N = int(input())
    P = [int(i) for i in input().split()]
    X = [int(i) for i in input().split()]
    return N, P, X

def is_possible(N, P, X):
    # Initialize the color and weight of the root vertex as white and 0
    color = [None] * (N + 1)
    weight = [0] * (N + 1)
    color[1] = "white"

    # Recursively allocate colors and weights to the vertices
    def dfs(u):
        nonlocal color, weight
        for v in range(u + 1, N + 1):
            if P[v] == u:
                dfs(v)
                if color[u] == color[v]:
                    weight[u] += weight[v]
                if weight[u] == X[u]:
                    color[u] = "black" if color[u] == "white" else "white"
        return
    dfs(1)

    # Check if the condition is satisfied
    for u in range(1, N + 1):
        if weight[u] != X[u]:
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


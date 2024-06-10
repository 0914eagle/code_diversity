
def get_input():
    N = int(input())
    parent = list(map(int, input().split()))
    X = list(map(int, input().split()))
    return N, parent, X

def dfs(N, parent, X, color, weight, vertex):
    if vertex == N:
        return
    dfs(N, parent, X, color, weight, vertex+1)
    if color == "black":
        weight += X[vertex]
    print(f"Set the color of Vertex {vertex+1} to {color} and its weight to {weight}.")
    dfs(N, parent, X, "white" if color == "black" else "black", weight, vertex+1)

def is_possible(N, parent, X):
    if X[1] != 0:
        return False
    for i in range(2, N+1):
        if X[i] < 0:
            return False
    return True

def main():
    N, parent, X = get_input()
    if not is_possible(N, parent, X):
        print("IMPOSSIBLE")
        return
    dfs(N, parent, X, "black", 0, 0)
    print("POSSIBLE")

if __name__ == '__main__':
    main()


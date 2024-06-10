
def is_possible(N, P, X):
    # Initialize the color and weight of the root vertex as white and 0
    color = [0] * (N + 1)
    weight = [0] * (N + 1)
    color[1] = 0
    weight[1] = 0

    # Iterate through the vertices in the order of their depth in the tree
    for i in range(2, N + 1):
        # Get the parent of the current vertex
        parent = P[i]

        # If the current vertex has a different color than its parent, assign it the same color as its parent
        if color[i] != color[parent]:
            color[i] = color[parent]

        # If the current vertex has a different weight than its parent, assign it the same weight as its parent
        if weight[i] != weight[parent]:
            weight[i] = weight[parent]

        # If the current vertex has a different color and weight than its parent, return False
        if color[i] != color[parent] and weight[i] != weight[parent]:
            return False

    # If all vertices have the same color and weight as their parent, return True
    return True

def main():
    N, P, X = map(int, input().split())
    print("POSSIBLE" if is_possible(N, P, X) else "IMPOSSIBLE")

if __name__ == '__main__':
    main()


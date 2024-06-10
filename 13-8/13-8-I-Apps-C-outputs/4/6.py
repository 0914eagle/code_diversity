
def is_possible(n, parents, x_sequence):
    # Initialize a dictionary to store the color and weight of each vertex
    color_weight = {}
    for i in range(1, n + 1):
        color_weight[i] = [None, 0]

    # Set the color and weight of the root vertex (Vertex 1)
    color_weight[1][0] = "white"
    color_weight[1][1] = x_sequence[1]

    # Recursively assign colors and weights to the remaining vertices
    for i in range(2, n + 1):
        parent = parents[i - 1]
        if color_weight[parent][0] == "white":
            color_weight[i][0] = "black"
        else:
            color_weight[i][0] = "white"
        color_weight[i][1] = x_sequence[i] - color_weight[parent][1]

    # Check if the total weight of the vertices with the same color as each vertex is equal to its weight
    for i in range(1, n + 1):
        if color_weight[i][1] != x_sequence[i]:
            return False
    return True

def main():
    n = int(input())
    parents = [int(x) for x in input().split()]
    x_sequence = [int(x) for x in input().split()]
    if is_possible(n, parents, x_sequence):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()


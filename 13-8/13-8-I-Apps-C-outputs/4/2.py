
def get_input():
    N = int(input())
    parents = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    return N, parents, weights

def is_possible(N, parents, weights):
    # Initialize the color of the root vertex as white
    colors = ["white"] * (N + 1)
    # Initialize the total weight of each vertex as 0
    total_weight = [0] * (N + 1)
    # Initialize the size of each subtree as 1
    size = [1] * (N + 1)

    for i in range(2, N + 1):
        # Get the parent of vertex i
        parent = parents[i - 1]
        # Get the weight of vertex i
        weight = weights[i - 1]
        # Update the color of vertex i based on the color of its parent
        colors[i] = "black" if colors[parent] == "white" else "white"
        # Update the total weight of vertex i based on the weight of its parent
        total_weight[i] = total_weight[parent] + weight
        # Update the size of vertex i based on the size of its parent
        size[i] = size[parent] + 1

    for i in range(2, N + 1):
        # Get the weight of vertex i
        weight = weights[i - 1]
        # Get the total weight of the subtree rooted at vertex i
        subtree_total_weight = total_weight[i]
        # Get the size of the subtree rooted at vertex i
        subtree_size = size[i]
        # Calculate the expected weight of the subtree rooted at vertex i
        expected_weight = subtree_size * weight
        # Check if the expected weight is equal to the actual weight of the subtree
        if expected_weight != subtree_total_weight:
            return False

    return True

def main():
    N, parents, weights = get_input()
    print("POSSIBLE" if is_possible(N, parents, weights) else "IMPOSSIBLE")

if __name__ == '__main__':
    main()


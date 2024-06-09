
import math
import random

def solve(n, trees, b, d):
    # Calculate the area of the boar's body
    boar_area = math.pi * b ** 2

    # Initialize the probability of not hitting a tree to 1
    probability = 1

    # Iterate over the trees
    for tree in trees:
        # Calculate the distance between the boar and the tree
        distance = math.sqrt((tree[0] - b) ** 2 + (tree[1] - b) ** 2)

        # Calculate the angle between the boar and the tree
        angle = math.atan2(tree[1] - b, tree[0] - b)

        # Calculate the area of overlap between the boar and the tree
        overlap_area = math.pi * min(distance, b + tree[2]) ** 2 - math.pi * max(distance - b - tree[2], 0) ** 2

        # Calculate the probability of not hitting the tree
        tree_probability = math.exp(-overlap_area / boar_area)

        # Update the probability of not hitting a tree
        probability *= tree_probability

    # Return the probability of not hitting a tree
    return probability

# Main function
if __name__ == "__main__":
    # Read the input
    n = int(input())
    trees = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        trees.append((x, y, r))
    b, d = map(int, input().split())

    # Solve the problem
    probability = solve(n, trees, b, d)

    # Print the output
    print(probability)


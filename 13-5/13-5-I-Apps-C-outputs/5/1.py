
import math
import random

def solve(n, b, d, trees):
    # Calculate the area of the boar's body
    boar_area = math.pi * b ** 2

    # Initialize the probability to 1
    prob = 1

    # Loop through each tree
    for tree in trees:
        # Calculate the distance between the boar and the tree
        dist = math.sqrt((tree[0] - b) ** 2 + (tree[1] - b) ** 2)

        # Check if the boar will hit the tree before it charges the full distance
        if dist < d:
            # Calculate the area of overlap between the boar and the tree
            overlap_area = math.pi * min(dist, b) ** 2

            # Subtract the probability of hitting the tree from the total probability
            prob -= overlap_area / boar_area

    # Return the probability of completing the charge without hitting a tree
    return prob

# Main function
if __name__ == "__main__":
    # Read the input
    n, b, d = map(int, input().split())
    trees = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        trees.append((x, y, r))

    # Solve the problem
    print(solve(n, b, d, trees))



import math
import random

def solve(n, trees, b, d):
    # Calculate the area of the boar's body
    boar_area = math.pi * b ** 2

    # Initialize the probability to 1
    probability = 1

    # Loop through each tree
    for i in range(n):
        # Calculate the distance between the boar and the tree
        dx = trees[i][0] - b
        dy = trees[i][1] - b
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Check if the boar will hit the tree before it charges the full distance
        if distance < d:
            # Calculate the area of overlap between the boar and the tree
            overlap_area = math.pi * min(b, trees[i][2]) ** 2

            # Subtract the probability of hitting the tree from the total probability
            probability -= overlap_area / boar_area

    # Return the probability of completing the charge without hitting a tree
    return probability

# Main function
if __name__ == "__main__":
    # Read the input
    n = int(input())
    trees = []
    for i in range(n):
        x, y, r = map(int, input().split())
        trees.append([x, y, r])
    b, d = map(int, input().split())

    # Solve the problem
    probability = solve(n, trees, b, d)

    # Print the output
    print(probability)


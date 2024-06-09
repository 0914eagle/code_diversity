
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
        distance = math.sqrt((trees[i][0] - b) ** 2 + (trees[i][1] - b) ** 2)

        # Calculate the probability of the boar hitting the tree
        hit_probability = math.exp(-(distance ** 2) / (2 * d ** 2))

        # Calculate the probability of the boar missing the tree
        miss_probability = 1 - hit_probability

        # Calculate the probability of the boar hitting a smaller tree first
        smaller_tree_probability = 0
        for j in range(n):
            if i != j and trees[j][2] < trees[i][2]:
                smaller_tree_probability += miss_probability * (trees[j][2] ** 2) / boar_area

        # Calculate the probability of the boar missing a smaller tree first
        larger_tree_probability = miss_probability * (trees[i][2] ** 2) / boar_area

        # Calculate the total probability of the boar missing the tree
        total_probability = smaller_tree_probability + larger_tree_probability

        # Update the probability
        probability *= total_probability

    return probability


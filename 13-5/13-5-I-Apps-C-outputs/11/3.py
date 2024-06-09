
import math
import random

def f1(n, b, d):
    # Calculate the area of the boar's body
    boar_area = math.pi * b ** 2

    # Initialize the probability of not hitting a tree to 1
    prob = 1.0

    # Loop through each tree
    for i in range(n):
        # Calculate the distance between the boar and the tree
        dist = math.sqrt((x[i] - 0) ** 2 + (y[i] - 0) ** 2)

        # If the boar is within the tree's radius, calculate the overlap area
        if dist <= r[i] + b:
            # Calculate the overlap area
            overlap_area = math.pi * min(r[i], dist) ** 2

            # Subtract the overlap area from the boar's body area
            boar_area -= overlap_area

            # If the boar's body area is less than or equal to 0, return 0
            if boar_area <= 0:
                return 0.0

    # Calculate the probability of not hitting a tree
    prob = 1 - (boar_area / (math.pi * b ** 2))

    return prob

def f2(n, b, d):
    # Initialize the probability of not hitting a tree to 1
    prob = 1.0

    # Loop through each tree
    for i in range(n):
        # Calculate the distance between the boar and the tree
        dist = math.sqrt((x[i] - 0) ** 2 + (y[i] - 0) ** 2)

        # If the boar is within the tree's radius, calculate the overlap area
        if dist <= r[i] + b:
            # Calculate the overlap area
            overlap_area = math.pi * min(r[i], dist) ** 2

            # Subtract the overlap area from the boar's body area
            boar_area -= overlap_area

            # If the boar's body area is less than or equal to 0, return 0
            if boar_area <= 0:
                return 0.0

    # Calculate the probability of not hitting a tree
    prob = 1 - (boar_area / (math.pi * b ** 2))

    return prob

if __name__ == '__main__':
    n = int(input())
    b = int(input())
    d = int(input())

    # Initialize the x and y coordinates of the trees
    x = []
    y = []

    # Loop through each tree
    for i in range(n):
        # Read the x and y coordinates of the tree
        xi, yi, ri = map(int, input().split())

        # Add the x and y coordinates to the lists
        x.append(xi)
        y.append(yi)

        # Add the radius of the tree to the list
        r.append(ri)

    # Calculate the probability of not hitting a tree
    prob = f1(n, b, d)

    # Print the probability
    print(prob)


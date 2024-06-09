
import itertools

def count_paintings(N, S1, S2):
    # Initialize a dictionary to store the number of paintings for each domino
    paintings = {}
    for domino in itertools.product("RGB", repeat=N):
        paintings[domino] = 0

    # Initialize a set to store the colors of the dominoes in the first row
    colors = set()

    # Iterate over the dominoes in the first row
    for i in range(N):
        # Get the color of the current domino
        color = S1[i]
        # If the color is not already in the set, add it to the set and increment the number of paintings for the current domino
        if color not in colors:
            colors.add(color)
            paintings[domino] += 1

    # Iterate over the dominoes in the second row
    for i in range(N):
        # Get the color of the current domino
        color = S2[i]
        # If the color is not already in the set, add it to the set and increment the number of paintings for the current domino
        if color not in colors:
            colors.add(color)
            paintings[domino] += 1

    # Return the number of paintings modulo 1000000007
    return sum(paintings.values()) % 1000000007

